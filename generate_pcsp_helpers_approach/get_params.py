from dateutil.relativedelta import relativedelta
import pandas as pd


def get_params_helper(df, hand):
    # Serve
    De_Serve = df.query('shot_type==1 and from_which_court==1')
    De_Serve_2nd = df.query('shot_type==2 and from_which_court==1')
    Ad_Serve = df.query('shot_type==1 and from_which_court==3')
    Ad_Serve_2nd = df.query('shot_type==2 and from_which_court==3')

    # Return
    De_ForeHandR = df.query(
        'shot_type==3 and prev_shot_from_which_court==1 and shot<=20'
    )
    Ad_ForeHandR = df.query(
        'shot_type==3 and prev_shot_from_which_court==3 and shot<=20'
    )
    De_BackHandR = df.query(
        'shot_type==3 and prev_shot_from_which_court==1 and shot<=40 and shot>20'
    )
    Ad_BackHandR = df.query(
        'shot_type==3 and prev_shot_from_which_court==3 and shot<=40 and shot>20'
    )

    # Stroke
    De_Stroke = df.query('shot_type==4 and from_which_court==1')
    Mid_Stroke = df.query('shot_type==4 and from_which_court==2')
    Ad_Stroke = df.query('shot_type==4 and from_which_court==3')
    De_Stroke_A = df.query('shot_type==4 and from_which_court==1 and prev_shot_approach_shot==1')
    Mid_Stroke_A = df.query('shot_type==4 and from_which_court==2 and prev_shot_approach_shot==1')
    Ad_Stroke_A = df.query('shot_type==4 and from_which_court==3 and prev_shot_approach_shot==1')
    De_Stroke_NLV = df.query('shot_type==4 and from_which_court==1 and prev_shot not in [5, 26, 11, 32, 15, 36]')
    Mid_Stroke_NLV = df.query('shot_type==4 and from_which_court==2 and prev_shot not in [5, 26, 11, 32, 15, 36]')
    Ad_Stroke_NLV = df.query('shot_type==4 and from_which_court==3 and prev_shot not in [5, 26, 11, 32, 15, 36]')

    results = []
    # Serve
    for Serve in [De_Serve, De_Serve_2nd, Ad_Serve, Ad_Serve_2nd]:
        ServeT = Serve.query('direction==6')
        ServeB = Serve.query('direction==5')
        ServeW = Serve.query('direction==4')
        serve_in = [len(x.query('shot_outcome==7'))
                    for x in [ServeT, ServeB, ServeW]]
        serve_win = [len(Serve.query('shot_outcome in [1, 5, 6]'))]
        serve_err = [len(Serve.query('shot_outcome in [2, 3, 4]'))]
        results.append(serve_in + serve_win + serve_err)

    # Return
    if hand == 'RH':  # RH
        directions = [[[[1], [1]], [[1], [3]], [[1], [2]]],                    # FH_[CC, DL, DM]
                      [[[2, 3], [3]], [[3], [1]], [[2], [1]], [
                          [2, 3], [2]]],  # FH_[IO, II, CC, DM]
                      [[[2], [3]], [[1], [3]], [[1, 2], [1]], [
                          [1, 2], [2]]],  # BH_[CC, II, IO, DM]
                      [[[3], [3]], [[3], [1]], [[3], [2]]]]                    # BH_[CC, DL, DM]
    else:  # LH
        directions = [[[[1, 2], [1]], [[1], [3]], [[2], [3]], [[1, 2], [2]]],  # FH_[IO, II, CC, DM]
                      # FH_[CC, DL, DM]
                      [[[3], [3]], [[3], [1]], [[3], [2]]],
                      # BH_[CC, DL, DM]
                      [[[1], [1]], [[1], [3]], [[1], [2]]],
                      [[[2], [1]], [[3], [1]], [[2, 3], [3]], [[2, 3], [2]]]]  # BH_[CC, II, IO, DM]
    for i, Return in enumerate([De_ForeHandR, Ad_ForeHandR, De_BackHandR, Ad_BackHandR]):
        shots = [Return.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[i]]
        return_in = [len(x.query('shot_outcome==7')) for x in shots]
        return_win = [len(Return.query('shot_outcome in [1, 5, 6]'))]
        return_err = [len(Return.query('shot_outcome in [2, 3, 4]'))]
        results.append(return_in + return_win + return_err)

    # Rally
    if hand == 'RH':  # RH
        directions = [[[1, 3, 2], [3, 1, 2]],  # de - FHCC, FHDL, FHDM, BHII, BHIO, BHDM
                      # mid - FHIO, FHCC, FHDM, BHIO, BHCC, BHDM
                      [[3, 1, 2], [1, 3, 2]],
                      [[3, 1, 2], [3, 1, 2]]]  # ad - FHIO, FHII, FHDM, BHCC, BHDL, BHDM

    else:  # LH
        directions = [[[1, 3, 2], [1, 3, 2]],  # de - FHIO, FHII, FHDM, BHCC, BHDL, BHDM
                      # mid - FHIO, FHCC, FHDM, BHIO, BHCC, BHDM
                      [[1, 3, 2], [3, 1, 2]],
                      [[3, 1, 2], [1, 3, 2]]]  # ad - FHCC, FHDL, FHDM, BHII, BHIO, BHDM
    for i, Stroke in enumerate([De_Stroke, Mid_Stroke, Ad_Stroke]):
        FH_Stroke_NA = Stroke.query('shot<=20 and approach_shot!=1')
        BH_Stroke_NA = Stroke.query('shot<=40 and shot>20 and approach_shot!=1')

        FH_Stroke_A = Stroke.query('shot<=20 and approach_shot==1')
        BH_Stroke_A = Stroke.query('shot<=40 and shot>20 and approach_shot==1')

        FH_shots_NA = [FH_Stroke_NA.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][0]]
        BH_shots_NA = [BH_Stroke_NA.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][1]]
        FH_shots_A = [FH_Stroke_A.query('to_which_court==@to_dir')
                         for to_dir in directions[i % 3][0]]
        BH_shots_A = [BH_Stroke_A.query('to_which_court==@to_dir')
                         for to_dir in directions[i % 3][1]]

        FH_stroke_in_NA = [len(x.query('shot_outcome==7'))
                                for x in FH_shots_NA]
        BH_stroke_in_NA = [len(x.query('shot_outcome==7'))
                                for x in BH_shots_NA]
        FH_stroke_in_A = [len(x.query('shot_outcome==7'))
                             for x in FH_shots_A]
        BH_stroke_in_A = [len(x.query('shot_outcome==7'))
                             for x in BH_shots_A]

        stroke_win = [len(Stroke.query('shot_outcome in [1, 5, 6]'))]
        stroke_err = [len(Stroke.query('shot_outcome in [2, 3, 4]'))]
        result = FH_stroke_in_NA + BH_stroke_in_NA + \
            FH_stroke_in_A + BH_stroke_in_A + stroke_win + stroke_err

        results.append(result)
    
    for i, Stroke in enumerate([De_Stroke_A, Mid_Stroke_A, Ad_Stroke_A]):
        FH_Stroke_LV = Stroke.query('shot<=20 and shot in [5, 15, 11]')
        BH_Stroke_LV = Stroke.query('shot<=40 and shot in [26, 32, 36]')

        FH_Stroke_NLV = Stroke.query('shot<=20 and shot not in [5, 11, 15]')
        BH_Stroke_NLV = Stroke.query('shot<=40 and shot>20 and shot not in [26, 32, 36]')

        FH_shots_LV  = [FH_Stroke_LV.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][0]]
        BH_shots_LV  = [BH_Stroke_LV.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][1]]
        FH_shots_NLV = [FH_Stroke_NLV.query('to_which_court==@to_dir')
                         for to_dir in directions[i % 3][0]]
        BH_shots_NLV = [BH_Stroke_NLV.query('to_which_court==@to_dir')
                         for to_dir in directions[i % 3][1]]

        FH_stroke_in_LV = [len(x.query('shot_outcome==7'))
                                for x in FH_shots_LV]
        BH_stroke_in_LV = [len(x.query('shot_outcome==7'))
                                for x in BH_shots_LV]
        FH_stroke_in_NLV = [len(x.query('shot_outcome==7'))
                             for x in FH_shots_NLV]
        BH_stroke_in_NLV = [len(x.query('shot_outcome==7'))
                             for x in BH_shots_NLV]

        stroke_win = [len(Stroke.query('shot_outcome in [1, 5, 6]'))]
        stroke_err = [len(Stroke.query('shot_outcome in [2, 3, 4]'))]
        result = FH_stroke_in_LV + BH_stroke_in_LV + \
            FH_stroke_in_NLV + BH_stroke_in_NLV + stroke_win + stroke_err

        results.append(result)

    for i, Stroke in enumerate([De_Stroke_NLV, Mid_Stroke_NLV, Ad_Stroke_NLV]):
        FH_Stroke_V = Stroke.query('shot<=20 and shot not in [5, 15]')
        BH_Stroke_V = Stroke.query('shot<=40 and shot>20 and shot not in [26, 36]')

        FH_shots_V = [FH_Stroke_V.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][0]]
        BH_shots_V = [BH_Stroke_V.query('to_which_court==@to_dir')
                            for to_dir in directions[i % 3][1]]

        FH_stroke_in_V = [len(x.query('shot_outcome==7'))
                                for x in FH_shots_V]
        BH_stroke_in_V = [len(x.query('shot_outcome==7'))
                                for x in BH_shots_V]

        stroke_win = [len(Stroke.query('(shot_outcome == 7 and shot in [5, 15, 26, 36]) or shot_outcome in [1, 5, 6]'))]
        stroke_err = [len(Stroke.query('shot_outcome in [2, 3, 4]'))]
        result = FH_stroke_in_V + BH_stroke_in_V + stroke_win + stroke_err

        results.append(result)

    return results


def get_params(data, date, ply1_name, ply2_name, ply1_hand, ply2_hand): 
    prev_date = (pd.to_datetime(date) -
                 relativedelta(years=2)).strftime('%Y-%m-%d')

    data_ply1 = data.query(
        'date>=@prev_date and date<@date and ply1_name==@ply1_name and ply2_name==@ply2_name')
    data_ply2 = data.query(
        'date>=@prev_date and date<@date and ply1_name==@ply2_name and ply2_name==@ply1_name')

    # number of matches played
    num_ply1_prev_n = len(data_ply1.date.unique())
    num_ply2_prev_n = len(data_ply2.date.unique())

    if num_ply1_prev_n == 0:
        data_ply1 = data.query(
            'date>=@prev_date and date<@date and ply1_name==@ply1_name and ply2_hand==@ply2_hand')
        
    if num_ply2_prev_n == 0:
        data_ply2 = data.query(
            'date>=@prev_date and date<@date and ply1_hand==@ply2_hand and ply2_name==@ply1_name')

    # get players params
    ply1_params = get_params_helper(data_ply1, ply1_hand)
    ply2_params = get_params_helper(data_ply2, ply2_hand)

    # sample
    params = sum(ply1_params, []) + sum(ply2_params, [])

    print('# P1 matches:', num_ply1_prev_n)
    print('# P2 matches:', num_ply2_prev_n)
    print(f"Generated {len(params)} probabilities.")

    return params

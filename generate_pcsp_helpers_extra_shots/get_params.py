from dateutil.relativedelta import relativedelta
import pandas as pd


def get_params_helper(df, hand):
    # Serve
    De_Serve = df.query('shot_type==1 and from_which_court==1')
    De_Serve_2nd = df.query('shot_type==2 and from_which_court==1')
    Ad_Serve = df.query('shot_type==1 and from_which_court==3')
    Ad_Serve_2nd = df.query('shot_type==2 and from_which_court==3')
    # Return
    De_ForeHandR = df.query('shot_type==3 and prev_shot_from_which_court==1 and shot<=20 and shot!=3')
    Ad_ForeHandR = df.query('shot_type==3 and prev_shot_from_which_court==3 and shot<=20 and shot!=3')
    De_ForeHandR1 = df.query('shot_type==3 and prev_shot_from_which_court==1 and shot==3')
    Ad_ForeHandR1 = df.query('shot_type==3 and prev_shot_from_which_court==3 and shot==3')
    De_BackHandR = df.query('shot_type==3 and prev_shot_from_which_court==1 and shot<=40 and shot>20 and shot!=24')
    Ad_BackHandR = df.query('shot_type==3 and prev_shot_from_which_court==3 and shot<=40 and shot>20 and shot!=24')
    De_BackHandR1 = df.query('shot_type==3 and prev_shot_from_which_court==1 and shot==24')
    Ad_BackHandR1 = df.query('shot_type==3 and prev_shot_from_which_court==3 and shot==24')
    # Stroke
    De_Stroke = df.query('shot_type==4 and from_which_court==1')
    Mid_Stroke = df.query('shot_type==4 and from_which_court==2')
    Ad_Stroke = df.query('shot_type==4 and from_which_court==3')

    results = []
    # Serve
    for Serve in [De_Serve, De_Serve_2nd, Ad_Serve, Ad_Serve_2nd]:
        ServeT = Serve.query('direction==6')
        ServeB = Serve.query('direction==5')
        ServeW = Serve.query('direction==4')
        serve_in = [len(x.query('shot_outcome==7')) for x in [ServeT, ServeB, ServeW]]
        serve_win = [len(Serve.query('shot_outcome in [1, 5, 6]'))]
        serve_err = [len(Serve.query('shot_outcome in [2, 3, 4]'))]
        results.append(serve_in + serve_win + serve_err)

    # Return
    if hand == 'RH':  # RH
        directions = [[[[1], [1]], [[1], [3]], [[1], [2]]],                    # FH_[CC, DL, DM]
                      [[[2, 3], [3]], [[3], [1]], [[2], [1]], [[2, 3], [2]]],  # FH_[IO, II, CC, DM]
                      [[[2], [3]], [[1], [3]], [[1, 2], [1]], [[1, 2], [2]]],  # BH_[CC, II, IO, DM]
                      [[[3], [3]], [[3], [1]], [[3], [2]]]]                    # BH_[CC, DL, DM]
    else:  # LH
        directions = [[[[1, 2], [1]], [[1], [3]], [[2], [3]], [[1, 2], [2]]],  # FH_[IO, II, CC, DM]
                      [[[3], [3]], [[3], [1]], [[3], [2]]],                    # FH_[CC, DL, DM]
                      [[[1], [1]], [[1], [3]], [[1], [2]]],                    # BH_[CC, DL, DM]
                      [[[2], [1]], [[3], [1]], [[2, 3], [3]], [[2, 3], [2]]]]  # BH_[CC, II, IO, DM]

    return_in = []
    shots = [De_ForeHandR.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[0]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    shots = [De_ForeHandR1.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[0]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    return_win = [len(De_ForeHandR.query('shot_outcome in [1, 5, 6]')) + len(De_ForeHandR1.query('shot_outcome in [1, 5, 6]'))]
    return_err = [len(De_ForeHandR.query('shot_outcome in [2, 3, 4]')) + len(De_ForeHandR1.query('shot_outcome in [2, 3, 4]'))]
    results.append(return_in + return_win + return_err)

    return_in = []
    shots = [Ad_ForeHandR.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[1]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    shots = [Ad_ForeHandR1.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[1]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    return_win = [len(Ad_ForeHandR.query('shot_outcome in [1, 5, 6]')) + len(Ad_ForeHandR1.query('shot_outcome in [1, 5, 6]'))]
    return_err = [len(Ad_ForeHandR.query('shot_outcome in [2, 3, 4]')) + len(Ad_ForeHandR1.query('shot_outcome in [2, 3, 4]'))]
    results.append(return_in + return_win + return_err)

    return_in = []
    shots = [De_BackHandR.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[2]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    shots = [De_BackHandR1.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[2]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    return_win = [len(De_BackHandR.query('shot_outcome in [1, 5, 6]')) + len(De_BackHandR1.query('shot_outcome in [1, 5, 6]'))]
    return_err = [len(De_BackHandR.query('shot_outcome in [2, 3, 4]')) + len(De_BackHandR1.query('shot_outcome in [2, 3, 4]'))]
    results.append(return_in + return_win + return_err)

    return_in = []
    shots = [Ad_BackHandR.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[3]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    shots = [Ad_BackHandR1.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[3]]
    return_in += [len(x.query('shot_outcome==7')) for x in shots]
    return_win = [len(Ad_BackHandR.query('shot_outcome in [1, 5, 6]')) + len(Ad_BackHandR1.query('shot_outcome in [1, 5, 6]'))]
    return_err = [len(Ad_BackHandR.query('shot_outcome in [2, 3, 4]')) + len(Ad_BackHandR1.query('shot_outcome in [2, 3, 4]'))]
    results.append(return_in + return_win + return_err)
    # for i, Return in enumerate([De_ForeHandR, Ad_ForeHandR, De_BackHandR, Ad_BackHandR]):
    #     shots = [Return.query('from_which_court in @dir[0] and to_which_court in @dir[1]') for dir in directions[i]]
    #     return_in = [len(x.query('shot_outcome==7')) for x in shots]
    #     return_win = [len(Return.query('shot_outcome in [1, 5, 6]'))]
    #     return_err = [len(Return.query('shot_outcome in [2, 3, 4]'))]
    #     results.append(return_in + return_win + return_err)

    # Rally
    if hand == 'RH':  # RH
        directions = [[[1, 3, 2], [3, 1, 2]], # de - FHCC, FHDL, FHDM, BHII, BHIO, BHDM
                      [[3, 1, 2], [1, 3, 2]], # mid - FHIO, FHCC, FHDM, BHIO, BHCC, BHDM
                      [[3, 1, 2], [3, 1, 2]]] # ad - FHIO, FHII, FHDM, BHCC, BHDL, BHDM

    else:  # LH
        directions = [[[1, 3, 2], [1, 3, 2]],  # de - FHIO, FHII, FHDM, BHCC, BHDL, BHDM
                      [[1, 3, 2], [3, 1, 2]],  # mid - FHIO, FHCC, FHDM, BHIO, BHCC, BHDM
                      [[3, 1, 2], [1, 3, 2]]]  # ad - FHCC, FHDL, FHDM, BHII, BHIO, BHDM
    for i, Stroke in enumerate([De_Stroke, Mid_Stroke, Ad_Stroke]):
        FH_Stroke = Stroke.query('shot<=20 and shot!=3')
        BH_Stroke = Stroke.query('shot<=40 and shot>20 and shot!=24')
        FHC_Stroke = Stroke.query('shot==3')
        BHC_Stroke = Stroke.query('shot==24')
        FHC_shots = [FHC_Stroke.query('to_which_court==@to_dir') for to_dir in directions[i][0]]
        BHC_shots = [BHC_Stroke.query('to_which_court==@to_dir') for to_dir in directions[i][1]]
        FH_shots = [FH_Stroke.query('to_which_court==@to_dir') for to_dir in directions[i][0]]
        BH_shots = [BH_Stroke.query('to_which_court==@to_dir') for to_dir in directions[i][1]]
        shots = FH_shots + BH_shots
        FH_stroke_in = [len(x.query('shot_outcome==7')) for x in FH_shots]
        BH_stroke_in = [len(x.query('shot_outcome==7')) for x in BH_shots]
        FHC_stroke_in = [len(x.query('shot_outcome==7')) for x in FHC_shots]
        BHC_stroke_in = [len(x.query('shot_outcome==7')) for x in BHC_shots]
        stroke_win = [len(Stroke.query('shot_outcome in [1, 5, 6]'))]
        stroke_err = [len(Stroke.query('shot_outcome in [2, 3, 4]'))]
        results.append(FH_stroke_in + BH_stroke_in + FHC_stroke_in + BHC_stroke_in + stroke_win + stroke_err)

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

# import os
# MY_API_KEY = os.environ.get('MY_API_KEY')

API_PATH = 'https://feeds.datagolf.com/'
FILE_FORMAT = 'json'

tour_lst = [
    'PGA',
    'OPP',
    'EUR',
    'KFT',
]

config = {
    'field_updates': {
        'path': 'field-updates',
        'fields': 
        [
            'dg_id',
            'player_name',
            'country',
            'event_name',
            'current_round',
            'dk_id',
            'dk_salary',
            'fd_id',
            'fd_salary',
            'yh_id',
            'yh_salary',
            'early_late',
            'last_updated',
        ],
    },
    'rankings': {
        'path':'preds/get-dg-rankings',
        'fields':
        [
            'dg_id',
            'primary_tour',
            'datagolf_rank',
            'owgr_rank',
            'dg_skill_estimate'
        ],
    },
    'pre_tourney_preds': {
        'path': 'preds/pre-tournament',
        'fields':
        [
            'dg_id',
            'make_cut_baseline',
            'top_10_baseline', 
            'top_20_baseline', 
            'top_5_baseline',
            'win_baseline',
        ],
    },
    'skill_decomps': {
        'path': 'preds/player-decompositions',
        'fields':
        [
            'dg_id',
            'baseline_pred', 
            'timing_adjustment',
            'age_adjustment',
            'strokes_gained_category_adjustment',
            'course_experience_adjustment',
            'course_history_adjustment', 
            'total_course_history_adjustment', 
            'total_fit_adjustment',
            'driving_accuracy_adjustment',
            'driving_distance_adjustment', 
            'other_fit_adjustment',
            'final_pred',
        ]
    },
    'odds':{
        'path': 'betting-tools/outrights',
        'fields': 
        [


        ]
    },    
    'historical_event_lst': {
        'path': 'historical-raw-data/event-list',
        'fields':
        [
            'calendar_year',
            'event_id',
        ]
    },
    'historical_round_data': {
        'path': 'historical-raw-data/rounds',
        'fields':
        [

        ]
    },
    'historical_odds': {
        'path': 'historical-odds/outrights',
        'fields':
        [
            'dg_id',
            'event_id',
            'year',
            'close_odds',
        ]
    }

}
# data.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



# ------ Muon Datasets ------ #
cpn.add_dataset(
    name='data_single_mu_A',
    id=1815011,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon/Run2018A-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=165,
    n_events=241600265, # this n_events is the gensumwt
    aux={
        'era': 'A',
        'run_range': (315257,316995),
    }
)
cpn.add_dataset(
    name='data_single_mu_B',
    id=1815012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon/Run2018B-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=108,
    n_events=119876473,
    aux={
        'era': 'B',
        'run_range': (317080,319310),
    }
)
cpn.add_dataset(
    name='data_single_mu_C',
    id=1815013,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon/Run2018C-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=96,
    n_events=110032072,
    aux={
        'era': 'C',
        'run_range': (319337,320065),
    }
)
cpn.add_dataset(
    name='data_single_mu_D',
    id=1815014,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon/Run2018D-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=371,
    n_events=513884680,
    aux={
        'era': 'D',
        'run_range': (320500,325175),
    }
)


# ------ EGamma Datasets ------ #
cpn.add_dataset(
    name='data_egamma_A',
    id=1815021,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        #'/EGamma/Run2018A-UL2018_NanoAODv15-v1/NANOAOD',
        '/EGamma/Run2018A-UL2018_NanoAODv15-v2/NANOAOD'
    ],
    n_files=307,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'A', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_egamma_B',
    id=1815022,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        #'/EGamma/Run2018B-UL2018_NanoAODv15-v1/NANOAOD',
        '/EGamma/Run2018B-UL2018_NanoAODv15-v2/NANOAOD'
    ],
    n_files=123,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'B', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_egamma_C',
    id=1815023,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        #'/EGamma/Run2018C-UL2018_NanoAODv15-v1/NANOAOD',
        '/EGamma/Run2018C-UL2018_NanoAODv15-v2/NANOAOD'
    ],
    n_files=153,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_egamma_D',
    id=1815024,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        #'/EGamma/Run2018D-UL2018_NanoAODv15-v1/NANOAOD',
        '/EGamma/Run2018D-UL2018_NanoAODv15-v2/NANOAOD'
    ],
    n_files=554,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 20162441} # n_events in aux is the nEvents produced
)

# ------- MuonEG Datasets ------- #
cpn.add_dataset(
    name='data_muoneg_A',
    id=1815031,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG/Run2018A-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=33,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'A', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_muoneg_B',
    id=1815032,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG/Run2018B-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=18,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'B', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_muoneg_C',
    id=1815033,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG/Run2018C-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=18,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_muoneg_D',
    id=1815034,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG/Run2018D-UL2018_NanoAODv15-v1/NANOAOD'],
    n_files=72,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 20162441} # n_events in aux is the nEvents produced
)

# ------- Tau Datasets ------- #
cpn.add_dataset(
    name='data_tau_A',
    id=1815041,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau/Run2018A-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=64,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'A', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_tau_B',
    id=1815042,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau/Run2018B-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=30,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'B', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_tau_C',
    id=1815043,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau/Run2018C-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=35,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 20162441} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='data_tau_D',
    id=1815044,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau/Run2018D-UL2018_NanoAODv15-v2/NANOAOD'],
    n_files=178,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 20162441} # n_events in aux is the nEvents produced
)

# tt.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022
# ID: 181501XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



cpn.add_dataset(
    name='tt_sl_powheg',
    id=18150101,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM'],
    n_files=589,
    n_events=155346152.0, # this n_events is the gensumwt
    aux={'n_events': 156612890} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_dl_powheg',
    id=18150102,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM'],
    n_files=169,
    n_events=47500385.0, # this n_events is the gensumwt
    aux={'n_events': 47887413} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_fh_powheg',
    id=18150103,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM'],
    n_files=407,
    n_events=105030029.0, # this n_events is the gensumwt
    aux={'n_events': 105888577} # n_events in aux is the nEvents produced
)

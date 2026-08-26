# ewk.py
# ID: 181504XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn


# NLO
cpn.add_dataset(
    name='ewk_wp_lnu_madgraph',
    id=18150401,
    is_data=False,
    processes=[procs.ewk_wp_lnu_m50toinf],
    keys=['/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=6,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='ewk_wm_lnu_madgraph',
    id=18150402,
    is_data=False,
    processes=[procs.ewk_wm_lnu_m50toinf],
    keys=['/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=7,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='ewk_z_ll_madgraph',
    id=18150403,
    is_data=False,
    processes=[procs.ewk_z_ll_m50toinf],
    keys=['/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=4,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)

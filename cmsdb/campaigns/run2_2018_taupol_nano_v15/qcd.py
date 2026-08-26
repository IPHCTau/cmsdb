# qcd.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



cpn.add_dataset(
    name='qcd',
    id=18150901,
    is_data=False,
    processes=[procs.qcd],
    keys=[],
    n_files=1,
    n_events=94639090.0, # this n_events is the gensumwt
    aux={'n_events': 94639090} # n_events in aux is the nEvents produced
)

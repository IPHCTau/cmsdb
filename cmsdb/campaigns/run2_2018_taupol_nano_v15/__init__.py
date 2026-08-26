# coding: utf-8

from order import Campaign


# ----------- #
#   Campaign  #
# ----------- #
campaign_run2_2018_taupol_nano_v15 = Campaign(
    name='run2_2018_taupol_nano_v15',
    id=181501,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 2,
        "year": 2018,
        "version": 15,
        "postfix": "",
        "custom": {
            "name": "run2_2018_taupol_nano_v15",
            "creator": "IPHC",
            "location": None,
            #"location": "/store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022",
            #"location": "/eos/cms/store/group/phys_tau/alebihan/taupola_noskim/Run2_2018",
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_taupol_nano_v15.data
import cmsdb.campaigns.run2_2018_taupol_nano_v15.dy
import cmsdb.campaigns.run2_2018_taupol_nano_v15.tt
import cmsdb.campaigns.run2_2018_taupol_nano_v15.st
import cmsdb.campaigns.run2_2018_taupol_nano_v15.wj
import cmsdb.campaigns.run2_2018_taupol_nano_v15.vv
import cmsdb.campaigns.run2_2018_taupol_nano_v15.higgs
import cmsdb.campaigns.run2_2018_taupol_nano_v15.ewk
import cmsdb.campaigns.run2_2018_taupol_nano_v15.qcd

# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads import test_config
from examples.docs import fixtures
import time

ad_account_id = test_config.account_id
campaign_group_id = fixtures.create_adcampaign().get_id()
product_catalog_id = test_config.product_catalog_id
product_set_id = test_config.product_set_id

# _DOC open [ADCAMPAIGN_CREATE_HOMEPAGE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign.update({
    AdCampaign.Field.name: 'Homepage Campaign',
    AdCampaign.Field.buying_type: AdCampaign.BuyingType.fixed_cpm,
    AdCampaign.Field.objective: AdCampaign.Objective.none,
    AdCampaign.Field.status: AdCampaign.Status.paused,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_HOMEPAGE]
campaign.remote_delete()


# _DOC open [ADCAMPAIGN_CREATE_VIDEO_VIEWS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign.update({
    AdCampaign.Field.name: 'Video Views Campaign',
    AdCampaign.Field.status: AdCampaign.Status.paused,
    AdCampaign.Field.objective: AdCampaign.Objective.video_views,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_VIDEO_VIEWS]
campaign.remote_delete()


# _DOC open [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign[AdCampaign.Field.name] = 'My First Campaign'
campaign[AdCampaign.Field.status] = AdCampaign.Status.paused
campaign[AdCampaign.Field.objective] = AdCampaign.Objective.website_conversions
campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
campaign.remote_delete()


# _DOC open [ADCAMPAIGN_GET_ADGROUPS]
# _DOC vars [campaign_group_id]
from facebookads.objects import AdCampaign, AdGroup

ad_campaign = AdCampaign(campaign_group_id)
ad_groups = ad_campaign.get_ad_groups(fields=[AdGroup.Field.name])

for ad_group in ad_groups:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADCAMPAIGN_GET_ADGROUPS]


# _DOC open [ADCAMPAIGN_GET_ADGROUPS_WITH_STATUS_ARCHIVED]
# _DOC vars [campaign_group_id]
from facebookads.objects import AdGroup, AdCampaign

adcampaign = AdCampaign(campaign_group_id)
params = {
    AdGroup.Field.status: [AdGroup.Status.archived],
}
adgroups = adcampaign.get_ad_groups(
    fields=[AdGroup.Field.name],
    params=params
)

for ad_group in adgroups:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADCAMPAIGN_GET_ADGROUPS_WITH_STATUS_ARCHIVED]


# _DOC open [ADCAMPAIGN_CREATE_LOCAL_AWARENESS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign.update({
    AdCampaign.Field.name: 'Local awareness campaign',
    AdCampaign.Field.status: AdCampaign.Status.paused,
    AdCampaign.Field.objective: AdCampaign.Objective.local_awareness,
})

campaign.remote_create()
# _DOC close [ADCAMPAIGN_CREATE_LOCAL_AWARENESS]
campaign.remote_delete()


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_DATE_PRESET]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign, Insights

campaign = AdCampaign(campaign_group_id)
params = {
    'date_preset': Insights.Preset.last_7_days,
}
insights = campaign.get_insights(params=params)
print(insights)
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_DATE_PRESET]


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_TIME_RANGES]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(campaign_group_id)
params = {
    'time_range': {
        'since': '2015-01-01',
        'until': '2015-01-20',
    },
}
insights = campaign.get_insights(params=params)
print(insights)
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_TIME_RANGES]


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_BREAKDOWNS]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(campaign_group_id)
params = {
    'breakdowns': [
        Insights.Breakdown.age,
        Insights.Breakdown.gender
    ]
}
insights = campaign.get_insights(params=params)
print(insights)
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_BREAKDOWNS]


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_ACTION_BREAKDOWNS]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(campaign_group_id)
params = {
    'action_breakdowns': [
        Insights.ActionBreakdown.action_destination,
        Insights.ActionBreakdown.action_type
    ]
}
insights = campaign.get_insights(params=params)
print(insights)
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_ACTION_BREAKDOWNS]


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_ACTIONS_REPORT_TIME]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(campaign_group_id)
params = {
    'action_report_time': 'conversion'
}
insights = campaign.get_insights(params=params)
print(insights)
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_ACTIONS_REPORT_TIME]


# _DOC open [ADCAMPAIGN_GET_INSIGHTS_ASYNC]
# _DOC vars [campaign_group_id:s]
from facebookads.objects import AdCampaign, Insights

campaign = AdCampaign(campaign_group_id)
params = {
    'level': Insights.Level.campaign_group
}
async_job = campaign.get_insights(params=params, async=True)

async_job.remote_read()

while async_job['async_percent_completion'] < 100:
    time.sleep(1)
    async_job.remote_read()

print(async_job.get_result())
# _DOC close [ADCAMPAIGN_GET_INSIGHTS_ASYNC]

# _DOC open [ADCAMPAIGN_CREATE_OBJECTIVE_PRODUCT_CATELOG_SALES]
# _DOC vars [ad_account_id:s, product_catalog_id]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign[AdCampaign.Field.name] = 'Product Catalog Sales Campaign Group'
campaign[AdCampaign.Field.status] = AdCampaign.Status.paused
objective = AdCampaign.Objective.product_catalog_sales
campaign[AdCampaign.Field.objective] = objective
campaign[AdCampaign.Field.promoted_object] = {
    'product_catalog_id': product_catalog_id
}

campaign.remote_create()
# _DOC close [ADCAMPAIGN_CREATE_OBJECTIVE_PRODUCT_CATELOG_SALES]
campaign.remote_delete()

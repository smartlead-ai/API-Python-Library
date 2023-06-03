import requests
from typing import Union, Literal, Dict, List


class Smartlead:
    """
    Python implementation of Smartlead API
        https://help.smartlead.ai/API-Documentation-a0d223bdd3154a77b3735497aad9419f
    """

    api_key = None

    class _V1:
        _base_url = 'https://server.smartlead.ai/api/v1'

        @staticmethod
        def endpoint(endpoint: str, query_params="") -> str:
            api_endpoint = endpoint if endpoint.startswith(
                '/') else f"/{endpoint}"
            api_key_suffix = f"?api_key={Smartlead.api_key}"
            return f"{Smartlead._V1._base_url}{api_endpoint}{api_key_suffix}{query_params}"

        class _CampaignsV1():
            def get(self, campaign_id: int):
                """
                This endpoint fetches a campaign based on its id.

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}'))
                return r.json()

            def create(self, name: str, client_id: Union[int, None]):
                """
                This endpoint creates a campaign

                ### Args:
                    * name (str): Name of campaign to be created
                    * client_id (int | None): The id of the client you want to associate with the campaign. If None, the campaign will be created without a client
                """
                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/create'), json={
                    'name': name,
                    'client_id': client_id
                })
                return r.json()

            def update_schedule(self, timezone: str, days_of_the_week: List[int], start_hour: str, end_hour: str, min_time_btw_emails: int, max_new_leads_per_day: int, schedule_start_time: str):
                """
                This endpoint updates a campaign's schedule.

                ### Args:
                    * timezone (str): The timezone of the campaign. This is used to determine the start and end hours of the campaign. Select from here: https://help.smartlead.ai/Timezones-20fcff9ddbb5441790c7c8e5ce0e9233
                    * days_of_the_week (List[int]): The days of the week you want to send emails. 0 is Sunday, 1 is Monday, and so on.
                    * start_hour (str): The hour of the day you want to start sending emails. This is in 24 hour format. For example, 9:00 AM is 09:00, and 5:00 PM is 17:00.
                    * end_hour (str): The hour of the day you want to stop sending emails. This is in 24 hour format. For example, 9:00 AM is 09:00, and 5:00 PM is 17:00.
                    * min_time_btw_emails (int): The minimum time between emails in minutes. For example, if you want to send emails every 2 minutes, set this to 2.
                    * max_new_leads_per_day (int): The maximum number of new leads you want to send emails to per day.
                    * schedule_start_time (str): The time you want to start the campaign. This is in standard ISO format. For example, 2021-01-01T00:00:00Z is January 1st, 2021 at 12:00 AM UTC.
                """
                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/create'), json={
                    'timezone': timezone,
                    'days_of_the_week': days_of_the_week,
                    'start_hour': start_hour,
                    'end_hour': end_hour,
                    'min_time_btw_emails': min_time_btw_emails,
                    'max_new_leads_per_day': max_new_leads_per_day,
                    'schedule_start_time': schedule_start_time,
                })
                return r.json()

            def update_settings(self, campaign_id: int, track_settings: List[Literal['DONT_TRACK_EMAIL_OPEN',  'DONT_TRACK_LINK_CLICK', 'DONT_TRACK_REPLY_TO_AN_EMAIL']], stop_lead_settings: List[Literal['REPLY_TO_AN_EMAIL', 'CLICK_ON_A_LINK', 'OPEN_AN_EMAIL']], unsubscribe_text: str, send_as_plain_text: bool, follow_up_percentage: int, client_id: Union[int, None]):
                """
                This endpoint updates a campaign's settings.

                ### Args:
                    * track_settings (List[Literal['DONT_TRACK_EMAIL_OPEN',  'DONT_TRACK_LINK_CLICK', 'DONT_TRACK_REPLY_TO_AN_EMAIL']]): The settings you want to track.
                    * stop_lead_settings (List[Literal['REPLY_TO_AN_EMAIL', 'CLICK_ON_A_LINK', 'OPEN_AN_EMAIL']]): The settings you want to stop a lead.
                    * unsubscribe_text (str): The text you want to use to unsubscribe from the campaign.
                    * send_as_plain_text (bool): Whether you want to send emails as plain text or not.
                    * follow_up_percentage (int): The percentage of leads you want to follow up with. For example, if you want to follow up with 50% of leads, set this to 50.
                    * client_id (int | None): The id of the client you want to associate with the campaign. If None, the campaign will have no client set.
                """
                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/{campaign_id}/settings'), json={
                    'track_settings': track_settings,
                    'stop_lead_settings': stop_lead_settings,
                    'unsubscribe_text': unsubscribe_text,
                    'send_as_plain_text': str(send_as_plain_text).lower(),
                    'follow_up_percentage': follow_up_percentage,
                    'client_id': client_id
                })
                return r.json()

            def get_sequences(self, campaign_id: int):
                """
                This endpoint fetches the sequence data of a campaign.

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch sequence data for.
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/sequences'))
                return r.json()

            def save_sequences(self, campaign_id: int, sequences: list):
                """
                This endpoint saves the sequence data of a campaign.

                ### Args:
                    * campaign_id (int): The id of the campaign you want to save sequence data for.
                    * sequences (list): The sequence data you want to save.
                """
                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/{campaign_id}/sequences'), json={
                    'sequences': sequences
                })
                return r.json()

            def all(self):
                """
                This endpoint fetches all the campaigns in your account
                """
                r = requests.get(Smartlead._V1.endpoint(f'/campaigns'))
                return r.json()

            def delete(self, campaign_id: int):
                """
                This endpoint deletes a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to delete
                """
                r = requests.delete(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}'))
                return r.json()

            def get_all_email_accounts(self, campaign_id: int):
                """
                This endpoint fetches all the email accounts in a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch email accounts for
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/email-accounts'))
                return r.json()

            def add_email_accounts(self, campaign_id: int, email_account_ids: List[int]):
                """
                This endpoint adds email accounts to a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to add email accounts to
                    * email_account_ids (List[int]): The ids of the email accounts you want to add
                """
                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/{campaign_id}/email-accounts'), json={
                    'email_account_ids': email_account_ids
                })
                return r.json()

            def remove_email_accounts(self, campaign_id: int, email_account_ids: List[int]):
                """
                This endpoint removes email accounts from a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to remove email accounts from
                    * email_account_ids (List[int]): The ids of the email accounts you want to remove
                """
                r = requests.delete(Smartlead._V1.endpoint(f'/campaigns/{campaign_id}/email-accounts'), json={
                    'email_account_ids': email_account_ids
                })
                return r.json()

            def get_leads(self, campaign_id: int, offset: int, limit: int):
                """
                This endpoint fetches all the leads in a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch leads for
                    * offset (int): The offset of the leads you want to fetch. For example, if you want to fetch leads from 10 to 20, set offset to 10.
                    * limit (int): The limit of the leads you want to fetch. For example, if you want to fetch 10 leads, set limit to 10.
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads', f'&offset={offset}&limit={limit}'))
                return r.json()

            def export_leads_data(self, campaign_id: int):
                """
                This endpoint exports all the leads in a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to export leads for
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads-export'))
                return r.json()

            def get_lead_message_history(self, campaign_id: int, lead_id: str):
                """
                This endpoint fetches the message history of a lead in a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch message history for
                    * lead_id (str): The id of the lead you want to fetch message history for
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads/{lead_id}/message-history'))
                return r.json()

            def get_statistics(self, campaign_id: int, offset: int, limit: int, email_sequence_number: Union[int, None] = None, email_status: Union[Literal['opened', 'clicked', 'replied', 'unsubscribed', 'bounced'], None] = None):
                """
                This endpoint fetches the statistics of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch statistics for
                    * offset (int): The offset of the statistics you want to fetch. For example, if you want to fetch statistics from 10 to 20, set offset to 10.
                    * limit (int): The limit of the statistics you want to fetch. For example, if you want to fetch 10 statistics, set limit to 10.
                    * email_sequence_number (int, optional): The email sequence number of the statistics you want to fetch. For example, if you want to fetch statistics for the first email sequence, set email_sequence_number to 1. Defaults to None.
                    * email_status (str, optional): The email status of the statistics you want to fetch. For example, if you want to fetch statistics for opened emails, set email_status to 'opened'. Defaults to None.
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/statistics', f'&offset={offset}&limit={limit}&email_sequence_number={email_sequence_number}&email_status={email_status}'))
                return r.json()

            def get_statistics_date_range(self, campaign_id: int, start_date: str, end_date: str):
                """
                This endpoint fetches the statistics of a campaign within a date range

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch statistics for
                    * start_date (str): The start date of the date range you want to fetch statistics for. For example, if you want to fetch statistics from 2021-01-01 to 2021-01-31, set start_date to '2021-01-01'.
                    * end_date (str): The end date of the date range you want to fetch statistics for. For example, if you want to fetch statistics from 2021-01-01 to 2021-01-31, set end_date to '2021-01-31'.
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/analytics-by-date', f'&start_date={start_date}&end_date={end_date}'))
                return r.json()

            def get_top_level_analytics(self, campaign_id: int):
                """
                This endpoint fetches the top level analytics of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch top level analytics for
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/analytics'))
                return r.json()

            def add_leads_to_campaign(self, campaign_id: int, lead_list: List[Dict]):
                """
                This endpoint adds leads to a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to add leads to
                    * lead_list (List[Dict]): The leads you want to add (max 100 leads per request)
                """

                r = requests.post(Smartlead._V1.endpoint(f'/campaigns/{campaign_id}/leads'), json={
                    'lead_list': lead_list
                })
                return r.json()

            def delete_lead_from_campaign(self, campaign_id: int, lead_id: int):
                """
                This endpoint deletes a lead from a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to delete a lead from
                    * lead_id (int): The id of the lead you want to delete
                """

                r = requests.delete(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads/{lead_id}'))
                return r.json()

            def unsubscribe_lead_from_campaign(self, campaign_id: int, lead_id: int):
                """
                This endpoint unsubscribes a lead from a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to unsubscribe a lead from
                    * lead_id (int): The id of the lead you want to unsubscribe
                """

                r = requests.post(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads/{lead_id}/unsubscribe'))
                return r.json()

            def update_lead_category(self, campaign_id: int, lead_id: int, category_id: int):
                """
                This endpoint updates the category of a lead in a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to update the category of a lead in
                    * lead_id (int): The id of the lead you want to update the category of
                    * category_id (int): The id of the category you want to update the lead to
                """

                r = requests.post(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/leads/{lead_id}/category'), json={
                        'category_id': category_id
                })
                return r.json()

            def update_status(self, campaign_id: int, status: Literal['PAUSED', 'STOPPED', 'START']):
                """
                This endpoint updates the status of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to update the status of
                    * status (Literal['PAUSED', 'STOPPED', 'START']): The status you want to update the campaign to
                """

                r = requests.post(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/status'), json={
                        'status': status
                })
                return r.json()

            def get_webhooks(self, campaign_id: int):
                """
                This endpoint fetches all the webhooks of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to fetch webhooks for
                """

                r = requests.get(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/webhooks'))
                return r.json()

            def update_webhook(self, campaign_id: int, webhook_id: int, name: str, webhook_url: str, event_types: List[Literal['EMAIL_SENT', 'EMAIL_OPEN', 'EMAIL_LINK_CLICK', 'EMAIL_REPLY', 'LEAD_UNSUBSCRIBED', 'LEAD_CATEGORY_UPDATED']], categories: List[Literal['Interested', 'Meeting Request', 'Not Interested', 'Do Not Contact', 'Information Request', 'Out Of Office', 'Wrong Person']]):
                """
                This endpoint updates a webhook of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to update a webhook of
                    * webhook_id (int): The id of the webhook you want to update
                    * name (str): The name of the webhook
                    * webhook_url (str): The url of the webhook
                    * event_types (List[Literal['EMAIL_SENT', 'EMAIL_OPEN', 'EMAIL_LINK_CLICK', 'EMAIL_REPLY', 'LEAD_UNSUBSCRIBED', 'LEAD_CATEGORY_UPDATED']]): The event types you want to subscribe to
                    * categories (List[Literal[]]): The categories you want to subscribe to
                """

                r = requests.post(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/webhooks'), json={
                        'id': webhook_id,
                        'name': name,
                        'webhook_url': webhook_url,
                        'event_types': event_types,
                        'categories': categories
                })
                return r.json()

            def delete_webhook(self, campaign_id: int, webhook_id: int):
                """
                This endpoint deletes a webhook of a campaign

                ### Args:
                    * campaign_id (int): The id of the campaign you want to delete a webhook of
                    * webhook_id (int): The id of the webhook you want to delete
                """

                r = requests.delete(Smartlead._V1.endpoint(
                    f'/campaigns/{campaign_id}/webhooks'), json={
                        'id': webhook_id
                })
                return r.json()

        class _LeadsV1():
            def get_campaigns(self, lead_id: int):
                """
                This endpoint fetches all the campaigns a lead is in

                ### Args:
                    * lead_id (int): The id of the lead you want to fetch campaigns for
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/leads/{lead_id}/campaigns'))
                return r.json()

            def get_categories(self):
                """
                This endpoint fetches all the categories in your account
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/leads/fetch-categories'))
                return r.json()

            def get_by_email_address(self, email_address: str):
                """
                This endpoint fetches a lead by email address

                ### Args:
                    * email_address (str): The email address of the lead you want to fetch
                """
                r = requests.get(Smartlead._V1.endpoint(
                    f'/leads', f'&email={email_address}'))
                return r.json()

            def unsubscribe_from_all_campaigns(self, lead_id: int):
                """
                This endpoint unsubscribes a lead from all campaigns

                ### Args:
                    * lead_id (int): The id of the lead you want to unsubscribe from all campaigns
                """
                r = requests.post(Smartlead._V1.endpoint(
                    f'/leads/{lead_id}/unsubscribe'))
                return r.json()

            def add_to_block_list(self, domain_block_list: List[str], client_id: Union[int, None]):
                """
                This endpoint adds domains to the block list

                ### Args:
                    * domain_block_list (List[str]): The domains you want to add to the block list
                    * client_id (int, optional): The id of the client you want to add the domains to the block list for. Defaults to None.
                """
                r = requests.post(Smartlead._V1.endpoint(
                    f'/leads/add-domain-block-list'), json={
                        'domain_block_list': domain_block_list,
                        'client_id': client_id
                })
                return r.json()

            def update(self, lead_id: int, lead_input: Dict):
                """
                This endpoint updates a lead

                ### Args:
                    * lead_id (int): The id of the lead you want to update
                    * lead_input (Dict): The updated lead information
                """
                r = requests.post(Smartlead._V1.endpoint(
                    f'/leads/{lead_id}'), json=lead_input)
                return r.json()

        class _EmailAccountsV1():
            def all(self):
                """
                This endpoint fetches all the email accounts in your account
                """
                r = requests.get(Smartlead._V1.endpoint(f'/email-accounts'))
                return r.json()

            def create(self, from_name: str, from_email: str, user_name: str, password: str, smtp_host: str, smtp_port: int, imap_host: str, imap_port: int, max_email_per_day: int, custom_tracking_url: str, bcc: str, signature: str, warmup_enabled: bool, total_warmup_per_day: Union[int, None], daily_rampup: Union[int, None], reply_rate_percentage: Union[int, None], client_id: Union[int, None]):
                """
                This endpoint updates an email account

                ### Args:
                    * from_name (str): The name you want to send emails from
                    * from_email (str): The email you want to send emails from
                    * user_name (str): The username of the email account
                    * password (str): The password of the email account
                    * smtp_host (str): The smtp host of the email account
                    * smtp_port (int): The smtp port of the email account
                    * imap_host (str): The imap host of the email account
                    * imap_port (int): The imap port of the email account
                    * max_email_per_day (int): The maximum number of emails you want to send per day
                    * custom_tracking_url (str): The custom tracking url you want to use
                    * bcc (str): The bcc you want to use
                    * signature (str): The signature you want to use
                    * warmup_enabled (bool): Whether you want to enable warmup or not
                    * total_warmup_per_day (int | None): The total number of emails you want to send per day during warmup
                    * daily_rampup (int | None): The number of emails you want to increase per day during warmup
                    * reply_rate_percentage (int | None): The percentage of replies you want to send during warmup
                    * client_id (int | None): The id of the client you want to associate with the email account. If None, the email account will have no client set.
                """
                r = requests.post(Smartlead._V1.endpoint(f'/email-accounts'), json={
                    'id': None,
                    'from_name': from_name,
                    'from_email': from_email,
                    'user_name': user_name,
                    'password': password,
                    'smtp_host': smtp_host,
                    'smtp_port': smtp_port,
                    'imap_host': imap_host,
                    'imap_port': imap_port,
                    'max_email_per_day': max_email_per_day,
                    'custom_tracking_url': custom_tracking_url,
                    'bcc': bcc,
                    'signature': signature,
                    'warmup_enabled': str(warmup_enabled).lower(),
                    'total_warmup_per_day': total_warmup_per_day,
                    'daily_rampup': daily_rampup,
                    'reply_rate_percentage': reply_rate_percentage,
                    'client_id': client_id
                })
                return r.json()

            def update(self, email_account_id: int, max_email_per_day: int, custom_tracking_url: str, bcc: str, signature: str, client_id: Union[int, None]):
                """
                This endpoint updates an email account

                ### Args:
                    * email_account_id (int): The id of the email account you want to update
                    * max_email_per_day (int): The maximum number of emails you want to send per day
                    * custom_tracking_url (str): The custom tracking url you want to use
                    * bcc (str): The bcc you want to use
                    * signature (str): The signature you want to use
                    * client_id (int | None): The id of the client you want to associate with the email account. If None, the email account will have no client set.
                """
                r = requests.post(Smartlead._V1.endpoint(f'/email-accounts/{email_account_id}'), json={
                    'max_email_per_day': max_email_per_day,
                    'custom_tracking_url': custom_tracking_url,
                    'bcc': bcc,
                    'signature': signature,
                    'client_id': client_id
                })
                return r.json()

            def set_warmup_settings(self, email_account_id: int, warmup_enabled: bool, total_warmup_per_day: int, daily_rampup: int, reply_rate_percentage: int):
                """
                This endpoint sets the warmup settings for an email account

                ### Args:
                    * email_account_id (int): The id of the email account you want to set warmup settings for
                    * warmup_enabled (bool): Whether you want to enable warmup or not
                    * total_warmup_per_day (int): The total number of emails you want to send per day during warmup
                    * daily_rampup (int): The number of emails you want to increase per day during warmup
                    * reply_rate_percentage (int): The percentage of replies you want to send during warmup
                """
                r = requests.post(Smartlead._V1.endpoint(f'/email-accounts/{email_account_id}/warmup'), json={
                    'warmup_enabled': str(warmup_enabled).lower(),
                    'total_warmup_per_day': total_warmup_per_day,
                    'daily_rampup': daily_rampup,
                    'reply_rate_percentage': reply_rate_percentage
                })
                return r.json()
            
            def reconnect_failed_email_accounts(self):
                """
                This endpoint reconnects failed email accounts. Rate limited to 3 times in a 24 hour period
                """
                r = requests.post(Smartlead._V1.endpoint(f'/email-accounts/reconnect-failed-email-accounts'))
                return r.json()
        
        class _ClientsV1():
            def create(self, name: str, email: str, permission: List[Literal['reply_master_inbox', 'full_access']], logo: str, logo_url: str, password: str):
                """
                This endpoint creates a client

                ### Args:
                    * name (str): The name of the client
                    * email (str): The email of the client
                    * permission (List[Literal['reply_master_inbox', 'full_access']]): The permissions of the client
                    * logo (str): The logo of the client
                    * logo_url (str): The logo url of the client
                    * password (str): The password of the client
                """
                r = requests.post(Smartlead._V1.endpoint(f'/client/save'), json={
                    'name': name,
                    'email': email,
                    'permission': permission,
                    'logo': logo,
                    'logo_url': logo_url,
                    'password': password
                })
                return r.json()
            
            def all(self):
                """
                This endpoint returns all clients
                """
                r = requests.get(Smartlead._V1.endpoint(f'/client'))
                return r.json()

        campaigns = _CampaignsV1()
        leads = _LeadsV1()
        email_accounts = _EmailAccountsV1()
        clients = _ClientsV1()

    v1 = _V1()

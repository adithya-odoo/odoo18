# -*- coding: utf-8 -*-

import datetime
import math

from odoo import api, models


class CrmLead(models.Model):
    """To create Dashboard"""
    _inherit = 'crm.lead'

    @api.model
    def get_tiles_data(self, value):
        """ Return the tile data"""
        company_id = self.env.company
        lead_domain = [('company_id', '=', company_id.id)]
        lost_domain = [('company_id', '=', company_id.id),
                       ('active', '=',  False)]
        if not value:
            lead_domain.append(('user_id', '=', self.env.user.id))
            lost_domain.append(('user_id', '=', self.env.user.id))
        leads = self.search(lead_domain)
        lost = self.search(lost_domain)

        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        sale_order = 0
        for i in my_opportunity.order_ids:
            sale_order += self.env['sale.order'].browse(i.ids).amount_invoiced
        won = leads.filtered(lambda r:r.stage_id.id == 4)
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        gcd = math.gcd(len(won),len(lost)) #greatest common division
        win_ratio = []
        if len(won) > 0 and len(lost) > 0:
            win_ratio.append(int(len(won) / gcd))
            win_ratio.append(int(len(lost) / gcd))
        else:
            win_ratio.append(len(won))
            win_ratio.append(len(lost))
        return {
            'total_leads': len(my_leads),
            'total_opportunity': len(my_opportunity),
            'expected_revenue': expected_revenue,
            'won' : len(won),
            'lost': len(lost),
            'currency': currency,
            'invoiced_amount': sale_order,
            'win_ratio': win_ratio,
        }

    @api.model
    def get_pie_data(self, value):
        """To return Activity data"""
        activity_domain = [('company_id', '=', self.env.company.id)]
        if not value:
            activity_domain.append(('user_id', '=', self.env.user.id))
        activities =  self.search(activity_domain)
        activity_name = []
        activity_len = []
        for data in activities.activity_type_id:
            activity_len.append(len(activities.filtered(lambda r: r.activity_type_id.id == data.id)))
            activity_name.append(data.name)
        return {
            'activity_name': activity_name,
            'activity_data':activity_len
        }

    @api.model
    def get_bar_data(self,value):
        """To return lost opportunity and lead"""
        lost_lead_domain = [('company_id', '=', self.env.company.id),
                            ('type', '=', 'lead'),
                            ('active', '=',  False)]
        lost_opportunity_domain = [('company_id', '=', self.env.company.id),
                                   ('type', '=', 'opportunity'),
                                   ('active', '=',  False)]
        if not value:
            lost_lead_domain.append(('user_id', '=', self.env.user.id))
            lost_opportunity_domain.append(('user_id', '=', self.env.user.id))
        lost_leads = len(self.search(lost_lead_domain))
        lost_opportunity = len(self.search(lost_opportunity_domain))

        return {
            'lost_leads':lost_leads,
            'lost_opportunity':lost_opportunity
        }

    @api.model
    def get_doughnut_data(self, value):
        """To return Medium data"""
        medium_domain = [('company_id', '=', self.env.company.id),
                         ('type', '=', 'lead')]
        if not value:
            medium_domain.append(('user_id', '=', self.env.user.id))
        medium = self.search(medium_domain)
        medium_name = []
        medium_len = []
        for data in medium.medium_id:
            medium_len.append(len(medium.filtered(
                lambda r: r.medium_id.id == data.id)))
            medium_name.append(data.name)
        return {
            'medium_name': medium_name,
            'medium_data': medium_len
        }

    @api.model
    def get_line_data(self, value):
        """To return campaign"""
        campaign_domain =[('company_id', '=', self.env.company.id),
                          ('type', '=', 'lead')]
        if not value:
            campaign_domain.append(('user_id', '=', self.env.user.id))
        campaign = self.search(campaign_domain)
        campaign_name = []
        campaign_len = []
        for data in campaign.campaign_id:
            campaign_len.append(len(campaign.filtered(
                lambda r: r.campaign_id.id == data.id)))
            campaign_name.append(data.name)
        return {
            'campaign_name': campaign_name,
            'campaign_data': campaign_len
        }

    @api.model
    def get_table_data(self, value):
        """To return month based lead"""
        lead_month_domain = [('company_id', '=', self.env.company.id),
                             ('type', '=', 'lead')]
        if not value:
            lead_month_domain.append(('user_id', '=', self.env.user.id))
        lead = self.search(lead_month_domain)
        lead_month = []
        lead_len = []
        checked_mnth = []
        for data in lead:
            if checked_mnth == 0 or data.create_date.month not in checked_mnth:
                lead_len.append(len(lead.filtered(
                    lambda r: r.create_date.month == data.create_date.month)))
                lead_month.append(data.create_date.month)
                checked_mnth.append(data.create_date.month)

        month = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        months = []
        for keys in month.keys():
            if keys in lead_month:
                months.append(month[keys])
        return {
            'months' : months,
            'lead_data' : lead_len
        }

    @api.model
    def get_filtered_data(self, value, filter_value):
        """To return filtered data"""
        today =datetime.datetime.now()
        company_id = self.env.company
        #tile data
        lead_domain = [('company_id', '=', company_id.id)]
        lost_domain = [('company_id', '=', company_id.id),
                       ('active', '=', False)]
        #bar data
        lost_lead_domain = [('company_id', '=', self.env.company.id),
                            ('type', '=', 'lead'),
                            ('active', '=', False)]
        lost_opportunity_domain = [('company_id', '=', self.env.company.id),
                                   ('type', '=', 'opportunity'),
                                   ('active', '=', False)]
        #pie data
        activity_domain = [('company_id', '=', self.env.company.id)]
        #doughnut data ,line data, table data
        medium_month_campaign_domain = [('company_id', '=', self.env.company.id),
                                        ('type', '=', 'lead')]
        total_lead = 0
        total_lost = 0
        total_lost_lead = 0
        total_lost_opportunity = 0

        if not value:
            lead_domain.append(('user_id', '=', self.env.user.id))
            lost_domain.append(('user_id', '=', self.env.user.id))
            #bar data
            lost_lead_domain.append(('user_id', '=', self.env.user.id))
            lost_opportunity_domain.append(('user_id', '=', self.env.user.id))
            #pie data
            activity_domain.append(('user_id', '=', self.env.user.id))
            # doughnut data, line data, table data
            medium_month_campaign_domain.append(('user_id', '=', self.env.user.id))
        if filter_value == 'today':
            #tile data
            total_lead = self.search(lead_domain).filtered(
                lambda r: (r.create_date.month == int(today.month) and
                           r.create_date.day == int(today.day) and
                           r.create_date.year == int(today.year)))
            total_lost = self.search(lost_domain).filtered(
                lambda r: (r.create_date.month == int(today.month) and
                           r.create_date.day == int(today.day) and
                           r.create_date.year == int(today.year)))
            # bar data
            total_lost_lead = len(self.search(lost_lead_domain).filtered(
                lambda r: (r.create_date.month == int(today.month) and
                           r.create_date.day == int(today.day) and
                           r.create_date.year == int(today.year))))
            total_lost_opportunity = len(
                self.search(lost_opportunity_domain).filtered(
                    lambda r: (r.create_date.month == int(today.month) and
                               r.create_date.day == int(today.day) and
                               r.create_date.year == int(today.year))))
            # pie data
            total_activity = self.search(activity_domain).filtered(
                lambda r: (r.create_date.month == int(today.month) and
                           r.create_date.day == int(today.day) and
                           r.create_date.year == int(today.year)))
            # doughnut data, line data
            total_medium_campaign = self.search(medium_month_campaign_domain).filtered(
                lambda r: (r.create_date.month == int(today.month) and
                           r.create_date.day == int(today.day) and
                           r.create_date.year == int(today.year)))
            #table data
            total_month = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m")))

        elif filter_value == 'this_week':
            total_lead = self.search(lead_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week))
            total_lost = self.search(lost_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week))
            #bar data
            total_lost_lead = len(self.search(lost_lead_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week)))
            total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week)))
            # pie data
            total_activity = self.search(activity_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week))
            # doughnut data, line data
            total_medium_campaign = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.isocalendar().week == int(today.isocalendar().week))
            #table data
            total_month = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.month == int(today.month))

        elif filter_value == 'this_month':
            total_lead = self.search(lead_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m")))
            total_lost = self.search(lost_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m")))
            #bar data
            total_lost_lead = len(self.search(lost_lead_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m"))))
            total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m"))))
            # pie data
            total_activity = self.search(activity_domain).filtered(lambda r:r.create_date.month == int(today.strftime("%m")))
            # doughnut data, line data
            total_medium_campaign = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m")))
            #table data
            total_month = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.month == int(today.strftime("%m")))

        elif filter_value == 'this_year':
            total_lead =  self.search(lead_domain).filtered(lambda r: r.create_date.year == int(today.year))
            total_lost =  self.search(lost_domain).filtered(lambda r: r.create_date.year == int(today.year))
            #bar data
            total_lost_lead = len(self.search(lost_lead_domain).filtered(lambda r: r.create_date.year == int(today.year)))
            total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(lambda r: r.create_date.year == int(today.year)))
            #pie data
            total_activity = self.search(activity_domain).filtered(lambda r:r.create_date.year == int(today.year))
            # doughnut data, line data
            total_medium_campaign = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.year == int(today.year))
            # table data
            total_month = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.year == int(today.year))

        elif filter_value == 'previous_year':
            total_lead = self.search(lead_domain).filtered(lambda r: r.create_date.year == int(today.year)-1)
            total_lost = self.search(lost_domain).filtered(lambda r: r.create_date.year == int(today.year)-1)
            # bar data
            total_lost_lead = len(self.search(lost_lead_domain).filtered(lambda r: r.create_date.year == int(today.year)-1))
            total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(lambda r: r.create_date.month == int(today.year)-1))
            # pie data
            total_activity = self.search(activity_domain).filtered(lambda r: r.create_date.year == int(today.year)-1)
            # doughnut data, line data
            total_medium_campaign = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.year == int(today.year)-1)
            # table data
            total_month = self.search(medium_month_campaign_domain).filtered(lambda r: r.create_date.year == int(today.year)-1)

        elif filter_value == 'quater':
            first_quater = [1, 2, 3, 4, 5, 6]
            second_quater = [7, 8, 9, 10, 11, 12]
            if today.month <= 6:
                total_lead = self.search(lead_domain).filtered(lambda r: r.create_date.month in first_quater)
                total_lost = self.search(lost_domain).filtered(lambda r: r.create_date.month in first_quater)
                # bar data
                total_lost_lead = len(self.search(lost_lead_domain).filtered(lambda r: r.create_date.month in first_quater))
                total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(
                    lambda r: r.create_date.month in first_quater))
                # pie data
                total_activity = self.search(activity_domain).filtered(
                    lambda r: r.create_date.month in first_quater)
                # doughnut data, line data
                total_medium_campaign = self.search(medium_month_campaign_domain).filtered(
                    lambda r: r.create_date.month in first_quater)
                # table data
                total_month = self.search(medium_month_campaign_domain).filtered(
                    lambda r: r.create_date.month in first_quater)
            else:
                total_lead = self.search(lead_domain).filtered(lambda r: r.create_date.month in second_quater)
                total_lost = self.search(lost_domain).filtered(lambda r: r.create_date.month in second_quater)
                # bar data
                total_lost_lead = len(
                    self.search(lost_lead_domain).filtered(lambda r: r.create_date.month in second_quater))
                total_lost_opportunity = len(self.search(lost_opportunity_domain).filtered(
                    lambda r: r.create_date.month in second_quater))
                # pie data
                total_activity = self.search(activity_domain).filtered(
                    lambda r: r.create_date.month in second_quater)
                # doughnut data, line data
                total_medium_campaign = self.search(medium_month_campaign_domain).filtered(
                    lambda r: r.create_date.month in second_quater)
                # table data
                total_month = self.search(medium_month_campaign_domain).filtered(
                    lambda r: r.create_date.month in second_quater)

        leads = total_lead
        lost = total_lost
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        sale_order = 0
        for i in my_opportunity.order_ids:
            sale_order += self.env['sale.order'].browse(i.ids).amount_invoiced
        won = leads.filtered(lambda r: r.stage_id.id == 4)
        gcd = math.gcd(len(won), len(lost))  # greatest common division
        win_ratio = []
        if len(won) > 0 and len(lost) > 0:
            win_ratio.append(int(len(won) / gcd))
            win_ratio.append(int(len(lost) / gcd))
        else:
            win_ratio.append(len(won))
            win_ratio.append(len(lost))
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

        lost_leads = total_lost_lead
        lost_opportunity = total_lost_opportunity

        activities = total_activity
        activity_name = []
        activity_len = []
        for data in activities.activity_type_id:
            activity_len.append(len(activities.filtered(
                lambda r: r.activity_type_id.id == data.id)))
            activity_name.append(data.name)

        medium = total_medium_campaign
        medium_name = []
        medium_len = []
        for data in medium.medium_id:
            medium_len.append(len(medium.filtered(
                lambda r: r.medium_id.id == data.id)))
            medium_name.append(data.name)

        campaign = total_medium_campaign
        campaign_name = []
        campaign_len = []
        for data in campaign.campaign_id:
            campaign_len.append(len(campaign.filtered(
                lambda r: r.campaign_id.id == data.id)))
            campaign_name.append(data.name)

        #table chart
        lead = total_month
        lead_month = []
        lead_len = []
        checked_mnth = []
        for data in lead:
            if checked_mnth == 0 or data.create_date.month not in checked_mnth:
                lead_len.append(len(lead.filtered(
                    lambda r: r.create_date.month == data.create_date.month)))
                lead_month.append(data.create_date.month)
                checked_mnth.append(data.create_date.month)

        month = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        months = []
        for keys in month.keys():
            if keys in lead_month:
                months.append(month[keys])

        return {
            'total_leads': len(my_leads),
            'total_opportunity': len(my_opportunity),
            'expected_revenue': expected_revenue,
            'won': len(won),
            'lost': len(lost),
            'currency': currency,
            'invoiced_amount': sale_order,
            'win_ratio': win_ratio,
            #barchart
            'lost_leads': lost_leads,
            'lost_opportunity': lost_opportunity,
            #pie chart
            'activity_name': activity_name,
            'activity_data': activity_len,
            #doghnut chart
            'medium_name': medium_name,
            'medium_data': medium_len,
            #line chart
            'campaign_name': campaign_name,
            'campaign_data': campaign_len,
            # table
            'months': months,
            'lead_data': lead_len,
        }

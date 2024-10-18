/**@odoo-module **/
import { loadBundle } from "@web/core/assets";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";
import { user } from "@web/core/user";
import { Component, onWillStart, useEffect, useState} from  "@odoo/owl";

const actionRegistry = registry.category("actions");
class CrmDashboard extends Component {
   setup() {
     this.findUser();
     this.orm = useService('orm')
     this.barChart = null
     this.pieChart = null
     this.doughnutChart = null
     this.lineChart = null
     this.state = useState({
            monthList: [],
            leadByMonth : [],
     });

     onWillStart(async () =>{
       await loadBundle("web.chartjs_lib");
       this._crm_data();
       this._tableChart();
       this.barChartGraph();
       this.pieChartGraph();
       this.doughnutChartGraph();
       this.lineChartGraph();
     });
   }
   async findUser(){
      this.isCrmManager = await user.hasGroup("sales_team.group_sale_manager");
      this.isCrmUser = await user.hasGroup("sales_team.group_sale_salesman_all_leads");
      this.isNormalUser = await user.hasGroup("sales_team.group_sale_salesman");
   }
   async _tableChart(){
      var value;
      if (this.isCrmManager == true){
            value = true
      }
      else{
            value = false
      }
      await this.orm.call("crm.lead", "get_table_data", [value], {}).then((result) =>{
           this.state.monthList = result.months
           this.state.leadByMonth = result.lead_data
      });
   }

   async _crm_data(){
      console.log(this.isCrmManager)
      var value;
      if (this.isCrmManager == true){
           value = true
      }
      else{
           value = false
      }
      await this.orm.call("crm.lead", "get_tiles_data", [value], {}).then((result) => {
            document.getElementById('my_lead').append(result.total_leads);
            document.getElementById('my_opportunity').append(result.total_opportunity);
            document.getElementById('revenue').append(result.currency + result.expected_revenue);
            if(this.isCrmManager || this.isCrmUser){
                 document.getElementById('invoiced_amount').append(result.currency + result.invoiced_amount);
            }
            document.getElementById('won').append(result.won);
            document.getElementById('lost').append(result.lost);
            document.getElementById('winRatio').append(result.win_ratio[0])
            document.getElementById('lostRatio').append(result.win_ratio[1])
      });
   };

   async barChartGraph(){
       var value;
       if (this.isCrmManager == true){
           value = true
       }
       else{
           value = false
       }
       await this.orm.call("crm.lead", "get_bar_data", [value], {}).then((result) => {
           var ctx = document.getElementById('bar_canvas');
           if(this.barChart){
               this.barChart.destroy()
           }
          // Create a barchart
           this.barChart = new Chart(ctx, {
               type: 'bar', // Choose the chart type (bar, line, pie, etc.)
               data: {
                  labels: ['Lead', 'Opportunity'], // X-axis labels
                  datasets: [{
                      data: [result.lost_leads, result.lost_opportunity], // Y-axis data
                      backgroundColor: [
                          '#CC0033', '#0033CC ', '#00CC33 ',
                          '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                          '#99CC00', '#FFFF33 ', '#FFFF33',
                      ],
                      label:'',
                      borderColor: [
                         '#CC0033', '#0033CC ', '#00CC33 ',
                         '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                         '#99CC00', '#FFFF33 ', '#FFFF33',
                      ],
                      borderWidth: 1
                  }]
               },
               options: {
                  scales: {
                        y: {
                             beginAtZero: true
                        }
                  }
               }
           });
       });
   }

   async pieChartGraph(){
     var value;
       if (this.isCrmManager == true){
         value = true
       }
       else{
         value = false
     }
     await this.orm.call("crm.lead", "get_pie_data", [value], {}).then((result) => {
         var ctx = document.getElementById('pie_canvas');
         if(this.pieChart){
             this.pieChart.destroy()
         }
        // Create a chart
        this.pieChart = new Chart(ctx, {
           type: 'pie', // Choose the chart type (bar, line, pie, etc.)
           data: {
               labels: result.activity_name, // X-axis labels
               datasets: [{
                   data: result.activity_data, // Y-axis data
                   backgroundColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderWidth: 1
               }]
           },
           options: {
              aspectRatio: 2
           }
        });

     });
   }

   async doughnutChartGraph(){
      var value;
      if (this.isCrmManager == true){
           value = true
      }
     else{
         value = false
     }
     await this.orm.call("crm.lead", "get_doughnut_data", [value], {}).then((result) => {
         var ctx = document.getElementById('doughnut_canvas');
         if(this.doughnutChart){
            this.doughnutChart.destroy()
         }
        // Create a chart
         this.doughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels:result.medium_name, // X-axis labels
                datasets: [{
                   data: result.medium_data, // Y-axis data
                   backgroundColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderWidth: 1
                }]
            },
            options: {
               aspectRatio: 2
            }
         });
     });
   }

   async lineChartGraph(){
      var value;
      if (this.isCrmManager == true){
           value = true
      }
      else{
         value = false
      }
      await this.orm.call("crm.lead", "get_line_data", [value], {}).then((result) => {
         var ctx = document.getElementById('line_canvas');
         if(this.lineChart){
            this.lineChart.destroy()
         }
         this.lineChart = new Chart(ctx, {
            type: 'line',
            data: {
               labels:  result.campaign_name, // X-axis labels
               datasets: [{
                   data: result.campaign_data, // Y-axis data
                   backgroundColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   label:'',
                   borderColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                       '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                       '#99CC00', '#FFFF33 ', '#FFFF33',

                   ],
                   borderWidth: 1
               }]
            },
            options: {
                aspectRatio: 2
            }
         });
      });
   }
   redirectToLeads() {
        let onClickDomain;
        if(this.isCrmManager == true){
           onClickDomain = [['type', '=', 'opportunity']]
        }
        else{
           onClickDomain = [["user_id", "=", user.userId],['type', '=', 'opportunity']]
        }
         this.env.services.action.doAction({
             type: 'ir.actions.act_window',
             name: 'Leads',
             res_model: 'crm.lead',
             views:[[false, "list"], [false, "form"]],
             target: 'current',
             domain : onClickDomain

         });
   }
   redirectToOpportunity(){
       let onClickDomain;
       if(this.isCrmManager == true){
          onClickDomain = [['type', '=', 'opportunity']]
       }
       else{
         onClickDomain = [["user_id", "=", user.userId],['type', '=', 'opportunity']]
       }
       this.env.services.action.doAction({
           type: 'ir.actions.act_window',
           name: 'Opportunity',
           res_model: 'crm.lead',
           views: [[false, "list"], [false, "form"]],
           target: 'current',
           domain : onClickDomain
       });
   }
// onchange function
   async onChangeFilter(){
      console.log("hwvhdhgdvhvdw")
      var value;
      if (this.isCrmManager == true){
           value = true
      }
      else{
         value = false
      }
      var filter_value = document.getElementById('filter').value
      if(filter_value != 'all'){
          document.getElementById('my_lead').innerHTML = ""
          document.getElementById('my_opportunity').innerHTML = ""
          document.getElementById('revenue').innerHTML = ""
          if(this.isCrmManager || this.isCrmUser){
               document.getElementById('invoiced_amount').innerHTML = "";
          }
          document.getElementById('won').innerHTML = ""
          document.getElementById('lost').innerHTML = ""
          document.getElementById('winRatio').innerHTML = ""
          document.getElementById('lostRatio').innerHTML = ""
          await this.orm.call("crm.lead", "get_filtered_data", [value, filter_value], {}).then((result) => {
             document.getElementById('my_lead').append(result.total_leads);
             document.getElementById('my_opportunity').append(result.total_opportunity);
             document.getElementById('revenue').append(result.currency + result.expected_revenue);
             if(this.isCrmManager || this.isCrmUser){
                  document.getElementById('invoiced_amount').append(result.currency + result.invoiced_amount);
             }
             document.getElementById('won').append(result.won);
             document.getElementById('lost').append(result.lost);
             document.getElementById('winRatio').append(result.win_ratio[0])
             document.getElementById('lostRatio').append(result.win_ratio[1])
             //    bar chart
             var ctx = document.getElementById('bar_canvas');
             if(this.barChart){
                  this.barChart.destroy()
             }
             this.barChart = new Chart(ctx, {
             type: 'bar', // Choose the chart type (bar, line, pie, etc.)
             data: {
                   labels: ['Lead', 'Opportunity'], // X-axis labels
                   datasets: [{
                   data: [result.lost_leads, result.lost_opportunity], // Y-axis data
                   backgroundColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                       '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                       '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   label:'',
                   borderColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                       '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                       '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderWidth: 1
             }]
          },
          options: {
               scales: {
                     y: {
                        beginAtZero: true
                     }
               }
          }
      });
        var ctx = document.getElementById('pie_canvas');
           if(this.pieChart){
             this.pieChart.destroy()
           }
          // Create a chart
           this.pieChart = new Chart(ctx, {
           type: 'pie', // Choose the chart type (bar, line, pie, etc.)
           data: {
               labels: result.activity_name, // X-axis labels
               datasets: [{
                   data: result.activity_data, // Y-axis data
                   backgroundColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderWidth: 1
               }]
           },
           options: {
              aspectRatio: 2
           }
        });
        var ctx = document.getElementById('doughnut_canvas');
        if(this.doughnutChart){
            this.doughnutChart.destroy()
        }
       // Create a chart
        this.doughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
               labels: result.medium_name, // X-axis labels
               datasets: [{
                   data: result.medium_data, // Y-axis data
                   backgroundColor: [
                        '#CC0033', '#0033CC ', '#00CC33 ',
                        '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                        '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                       '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                       '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   borderWidth: 1
               }]
            },
            options: {
               aspectRatio: 2
            }
        });
        var ctx = document.getElementById('line_canvas');
        if(this.lineChart){
            this.lineChart.destroy()
        }
       // Create a chart
       this.lineChart = new Chart(ctx, {
           type: 'line',
           data: {
               labels: result.campaign_name, // X-axis labels
               datasets: [{
                   data: result.campaign_data, // Y-axis data
                   backgroundColor: [
                      '#CC0033', '#0033CC ', '#00CC33 ',
                      '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                      '#99CC00', '#FFFF33 ', '#FFFF33',
                   ],
                   label:'',
                   borderColor: [
                       '#CC0033', '#0033CC ', '#00CC33 ',
                       '#FF0000', '#00FFFF ', '#660066 ', '#990000 ',
                       '#99CC00', '#FFFF33 ', '#FFFF33',

                   ],
                   borderWidth: 1
               }]
           },
           options: {
              aspectRatio: 2
           }
       });
        this.state.monthList = result.months
        this.state.leadByMonth = result.lead_data
      });
   }
   else{
      document.getElementById('my_lead').innerHTML = ""
      document.getElementById('my_opportunity').innerHTML = ""
      document.getElementById('revenue').innerHTML = ""
      document.getElementById('invoiced_amount').innerHTML = ""
      document.getElementById('won').innerHTML = ""
      document.getElementById('lost').innerHTML = ""
      document.getElementById('winRatio').innerHTML = ""
      document.getElementById('lostRatio').innerHTML = ""
      this._crm_data();
      this._tableChart();
      this.barChartGraph();
      this.pieChartGraph();
      this.doughnutChartGraph();
      this.lineChartGraph();
   }
}
}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
//  Tag name that we entered in the first step.
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
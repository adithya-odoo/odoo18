/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { makeAwaitable, ask } from "@point_of_sale/app/store/make_awaitable_dialog";
import { useState } from "@odoo/owl";


patch(ControlButtons.prototype, {
     async onTypeClick() {
          console.log(this)
          var selectionList = []
          for(let i=0; i <this.pos.config.iface_available_categ_ids.length; i++){
               selectionList.push({label:this.pos.config.iface_available_categ_ids[i].name,
                                   item:this.pos.config.iface_available_categ_ids[i].name})
          }
          this.props.selectedValue = await makeAwaitable(this.dialog, SelectionPopup, {
             title: "Select your order type",
             list: selectionList,
          });
         console.log(this)
     },
});
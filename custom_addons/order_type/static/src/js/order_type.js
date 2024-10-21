/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";


patch(ControlButtons.prototype, {
     async onTypeClick() {
          console.log(this)
           const selectionList = this.pos.config.iface_available_categ_ids.map((iface_available_categ_ids) => ({
                id: iface_available_categ_ids.id,
                label: iface_available_categ_ids.name,
                item: iface_available_categ_ids.name,
            }));
          this.selectedValue = await makeAwaitable(this.dialog, SelectionPopup, {
             title: "Select your order type",
             list: selectionList,
          });
         this.pos.get_order().order_type = this.selectedValue
     },
});
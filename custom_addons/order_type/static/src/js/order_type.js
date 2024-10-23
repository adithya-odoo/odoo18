/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";


patch(ControlButtons.prototype, {
     async onTypeClick() {
          console.log(this.pos.config.order_type_ids)
           const selectionList = this.pos.config.order_type_ids.map((order_type_ids) => ({
                id: order_type_ids.id,
                label: order_type_ids.name,
                item: order_type_ids,
            }));
          this.selectedValue = await makeAwaitable(this.dialog, SelectionPopup, {
             title: "Select your order type",
             list: selectionList,
          });
          console.log(this.selectedValue)
         this.pos.get_order().order_type_id = this.selectedValue
     },
});
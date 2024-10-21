/** @odoo-module */

import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
  export_for_printing(baseUrl, headerData) {
        const result = super.export_for_printing(...arguments);
        console.log(this.order_type,"nnhbhbhehb")
        result.headerData.orderType = this.order_type;
        console.log(result,"jnnn")
        return result;
  },
});

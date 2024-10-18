/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import { Component, useState } from "@odoo/owl";

export class FloatToInteger extends Component {
   static template = 'web.FloatToInteger';
   static defaultProps = {
        inputType: "text",
    };

   setup() {
        this.state = useState({ value: 0});
        this.inputRef = useInputField({
            getValue: () => this.getValue,
            refName: "numpadInteger",
    });
    }

   get getValue() {
        const floatValue = parseFloat(this.props.record.data.float_to_integer);
        if (!isNaN(floatValue)) {
           return this.state.value = Math.round(floatValue);
        } else {
           return this.state.value = 0;
            }
        }
    }

export const FloatToIntegers = {
    component: FloatToInteger,
    supportedTypes: ["float"],
    displayName: _t("Float To Integer"),
};
registry.category("fields").add("float_to_integer", FloatToIntegers);

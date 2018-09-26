frappe.ui.form.on("Sales Order", {
    onload:  function(frm) {
        //if(frm.doc.delivery_date=='' || frm.doc.delivery_date == undefined){
        if(frm.doc.delivery_date==''){
            setDeliveryDate(frm);
        }
    },
    refresh:  function(frm) {
        if(!frm.doc.__islocal) {
            cur_frm.add_custom_button(__('Purchase Order Report'), function() {
                frappe.set_route("Report", "Purchase Order", "Purchase Order Report", {"sales_order":frm.doc.name});
            });
        }
    },
    transaction_date: function(frm, cdt, cdn){
        setDeliveryDate(frm);
    }
});

var setDeliveryDate= function(frm){
    cur_frm.set_value('delivery_date', frappe.datetime.add_months(frm.doc.transaction_date, 6));
}
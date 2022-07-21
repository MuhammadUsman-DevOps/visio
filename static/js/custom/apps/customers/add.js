"use strict";
var KTModalCustomersAdd = function () {
    var t, e, o, n, r, i;
    return {
        init: function () {
            i = new bootstrap.Modal(document.querySelector("#kt_modal_add_customer")), r = document.querySelector("#kt_modal_add_customer_form"), t = r.querySelector("#kt_modal_add_customer_submit"), e = r.querySelector("#kt_modal_add_customer_cancel"), o = r.querySelector("#kt_modal_add_customer_close"), n = FormValidation.formValidation(r, {
                fields: {
                    full_name: {validators: {notEmpty: {message: "Customer name is required"}}},
                    email_address: {validators: {notEmpty: {message: "Customer email is required"}}},
                    "first-name": {validators: {notEmpty: {message: "First name is required"}}},
                    "last-name": {validators: {notEmpty: {message: "Last name is required"}}},
                    country: {validators: {notEmpty: {message: "Country is required"}}},
                    phone_number: {validators: {notEmpty: {message: "phone number is required"}}},
                    address: {validators: {notEmpty: {message: "Address 1 is required"}}},
                    city: {validators: {notEmpty: {message: "City is required"}}},
                    state: {validators: {notEmpty: {message: "State is required"}}},
                    postcode: {validators: {notEmpty: {message: "Postcode is required"}}},
                    contact_person_name: {validators: {notEmpty: {message: "Contact person name is required"}}},
                    contact_email_address: {validators: {notEmpty: {message: "Contact email address is required"}}},
                    contact_phone_number: {validators: {notEmpty: {message: "Contact phone is required"}}}
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger,
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            }), $(r.querySelector('[name="country"]')).on("change", (function () {
                n.revalidateField("country")
            })), t.addEventListener("click", (function (e) {
                e.preventDefault(), n && n.validate().then((function (e) {
                    console.log("validated!"), "Valid" == e ? (t.setAttribute("data-kt-indicator", "on"), t.disabled = !0, setTimeout((function () {
                        t.removeAttribute("data-kt-indicator"), $("#kt_modal_add_customer_form").submit()
                    }), 2e3)) : Swal.fire({
                        text: "Sorry, looks like there are some errors detected, please try again.",
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass: {confirmButton: "btn btn-primary"}
                    })
                }))
            })), e.addEventListener("click", (function (t) {
                t.preventDefault(), Swal.fire({
                    text: "Are you sure you would like to cancel?",
                    icon: "warning",
                    showCancelButton: !0,
                    buttonsStyling: !1,
                    confirmButtonText: "Yes, cancel it!",
                    cancelButtonText: "No, return",
                    customClass: {confirmButton: "btn btn-primary", cancelButton: "btn btn-active-light"}
                }).then((function (t) {
                    t.value ? (r.reset(), i.hide()) : "cancel" === t.dismiss && Swal.fire({
                        text: "Your form has not been cancelled!.",
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass: {confirmButton: "btn btn-primary"}
                    })
                }))
            })), o.addEventListener("click", (function (t) {
                t.preventDefault(), Swal.fire({
                    text: "Are you sure you would like to cancel?",
                    icon: "warning",
                    showCancelButton: !0,
                    buttonsStyling: !1,
                    confirmButtonText: "Yes, cancel it!",
                    cancelButtonText: "No, return",
                    customClass: {confirmButton: "btn btn-primary", cancelButton: "btn btn-active-light"}
                }).then((function (t) {
                    t.value ? (r.reset(), i.hide()) : "cancel" === t.dismiss && Swal.fire({
                        text: "Your form has not been cancelled!.",
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass: {confirmButton: "btn btn-primary"}
                    })
                }))
            }))
        }
    }
}();
KTUtil.onDOMContentLoaded((function () {
    KTModalCustomersAdd.init()
}));
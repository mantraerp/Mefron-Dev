// frappe.ui.form.on("Purchase Order", {
//     onload: function (frm) {
//         frm.set_query("set_warehouse", () => {
//             return {
//                 filters: {
//                     custom_is_purchase_warehouse: 1,
//                 },
//             };
//         });
//         frm.set_query("set_from_warehouse", () => {
//             return {
//                 filters: {
//                     custom_is_purchase_warehouse: 1,
//                 },
//             };
//         });
//         frm.set_query("supplier_warehouse", () => {
//             return {
//                 filters: {
//                     custom_is_subcontracting_warehouse: 1,
//                 },
//             };
//         });
//             // setTimeout(() => {
//             //     frm.set_query("supplier", () => {
//             //         return {
//             //             filters: {
//             //                 workflow_state: "Approved",
//             //             },
//             //         };
//             //     });
//             // }, 1000); // 1000 milliseconds = 1 second
//         if (frappe.user_roles.includes("System Manager") == false) {
//             setTimeout(() => {
//                 console.log("View Hide");
//                 frm.remove_custom_button("Update Items");
//             }, 0);
//         }
//     },
// });
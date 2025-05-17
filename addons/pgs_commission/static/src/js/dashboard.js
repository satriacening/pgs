/** @odoo-module */


import { CRMDashboard } from '@crm_dashboard/js/crm_dashboard'; // Ganti path sesuai modul asli Anda
import { jsonrpc } from "@web/core/network/rpc_service";
import { registry } from "@web/core/registry";

export class CRMDashboardExtended extends CRMDashboard {
    async onWillStart() {
        await super.onWillStart();  // Jalankan logika asal

        // Tambahkan data commission_report Anda
        this.commission_report = [
            ['John Doe', 'SO001', 1000, 100, '2025-05-01'],
            ['Jane Smith', 'SO002', 2000, 200, '2025-05-03'],
            ['Alice Brown', 'SO003', 1500, 150, '2025-05-10'],
        ];
    }
}

// Ganti component default jika dibutuhkan
registry.category("actions").add("pgs_commission.crm_dashboard", CRMDashboardExtended);

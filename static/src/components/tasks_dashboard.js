/** @odoo-module */

import {registry} from "@web/core/registry"
import {KpiCard} from "./kpi_card/kpi_card"
import {useService} from "@web/core/utils/hooks"

const {Component, onWillStart, useState} = owl

export class ProjectTaskDashboard extends Component {
    setup() {
        this.state = useState({
            task_count: {
                value: 10,
            },
            period: 365,
            selectedUser: '',
            userNames: [],
        })
        this.orm = useService("orm")
        this.actionService = useService("action")

        onWillStart(async () => {
            this.getDates()
            await this.getProjectTasksCount()
            await this.fetchUserNames()
        })
    }

    async onChangePeriod() {
        this.getDates()
        await this.getProjectTasksCount()
    }

    async onChangeUser() {
        this.getDates()
        await this.getProjectTasksCount()
    }

    getDates() {
        this.state.current_date = moment().subtract(this.state.period, 'days').format('YYYY-MM-DD')
        console.log(this.state.current_date)
    }

    async getProjectTasksCount() {
        let domain = [['stage_id', 'in', [1, 2, 10]]]; // new, done, in-progress

        if (this.state.selectedUser) {
            domain.push(['user_ids', 'in', [this.state.selectedUser]]);
        }

        if (this.state.period > 0) {
            domain.push(['date_deadline', '>=', this.state.current_date]);
        }

        const data = await this.orm.searchCount("project.task", domain);
        this.state.task_count.value = data;
    }

    async fetchUserNames() {
        const userRecords = await this.orm.searchRead("res.users", [], ['id', 'name']); // Fetch user IDs along with names
        this.state.userNames = userRecords.map(user => ({id: user.id, name: user.name}));
    }

    async viewTasks() {
        let domain = [['stage_id', 'in', [1, 2, 10]]]
        if (this.state.period > 0) {
            domain.push(['date_deadline', '>', this.state.current_date])
        }

        if (this.state.selectedUser) {
            domain.push(['user_ids', 'in', [this.state.selectedUser]]);
        }

        let list_view = await this.orm.searchRead("ir.model.data", [['name', '=', 'view_task_tree2']], ['res_id'])

        this.actionService.doAction({
            type: "ir.actions.act_window",
            name: "Task Count",
            res_model: "project.task",
            domain,
            views: [
                [list_view.length > 0 ? list_view[0].res_id : false, "list"],
                [false, "form"],
            ]
        })
    }
}

ProjectTaskDashboard.template = "owl.ProjectTaskDashboard"
ProjectTaskDashboard.components = {KpiCard}
registry.category("actions").add("owl.project_tasks_dashboard", ProjectTaskDashboard)

# Forget Me Not (FMN)
## Goal
A Discord calendar and reminder bot - that can be used across multiple servers.

## Main principles
- Every server is completely isolated.
- Modern Discord UI (buttons, dropdowns, modals).
- Service-based architecture.
- Easy to expand.

## Feature list
- **Calendar**
    - Add/edit/delete/archive/restore event
    - Search events (by title/date/user/participants/description)
    - Make recurring (daily/weekly/monthly/yearly/custom interval) events
    - View list of events (per day/week/month/date range)
    - Add reminders (1 day/1 week/3 hours/1 hours/15 minutes) with delivery via DM/chanel (to be chosen by user)
    - Add events participants
    - export (JSON/CSV)
    - **Birthdays**
        - Add/edit/remove birthdays
        - List upcoming birthdays
        - Birthday role
        - Birthday message
        - Birthday reminders
- **Statistics**
    - Events this day/week/month
    - Most active members
    - Busiest weekday
    - Total archived
    - Reminder usage statistics
- **Audit log (Admin only)**
    - Every action becomes:
        - Created event
        - Edited title
        - Changed category
        - Added participant
        - Removed participant
        - Reminder sent
        - Reminder failed
        - Birthday added
        - Timezone changed
        - Export created
    - Admins can search by
        - User
        - Event
        - Date
        - Action
    

## Installation

**Dependencies:** `base`, `mail`, `sale` (all core Odoo modules — no third-party dependencies).

1. Copy (or clone) the `digizilla` folder into your Odoo `addons` path.
2. Update the apps list: Settings → Apps → Update Apps List (developer mode required), or from the CLI:
   ```
   odoo -c /etc/odoo/odoo.conf -d <your_db> -i digizilla --stop-after-init
   ```
3. Log in as a user in the `Digizillians` group to access the app (Settings → Users & Companies → Groups → Digizillians → Users tab, to assign it).

## Design notes / assumptions

- **`sale_order_count` is computed, not `related`.** "No. of Sales Orders" isn't a field that exists on `res.partner` in a directly related-field sense — it has to be derived via `search_count` on `sale.order`. `related` only works when the target field already exists on the related model; since we're deriving a count rather than pulling through an existing value, `compute` is the correct tool.

- **`tag_ids` uses a small custom `digizilla.tag` model** rather than reusing `res.partner.category`, since the spec doesn't specify reusing an existing tag model, and a dedicated model keeps the addon self-contained with no assumptions about how `res.partner.category` might already be configured.

- **`age` is `store=True`** so it's usable for sorting/grouping/searching in list, kanban, and pivot views without extra configuration — a computed-but-unstored field can't be used that way by default.

- **Odoo 19 breaking changes encountered and handled:**
  - `res.groups.category_id` was removed in Odoo 19 in favor of `privilege_id` referencing a new `res.groups.privilege` model — the security group definition uses the new structure.
  - `_sql_constraints` is deprecated in favor of `models.Constraint` — the module currently still uses the older syntax (functional, generates a deprecation warning, not a hard error); noted here as a known item rather than left unexplained.
  - QWeb kanban templates in Odoo 19 use `t-name="card"` rather than the older `t-name="kanban-box"`.

## Deliverable

Git repository: `https://github.com/Roaa-838/digizilla_assessment`

# Project: Must/Want Task Manager for Students
Target User: University students.
Concept: "Smart & Modern Blue" - Balancing academic obligations (Must) and personal desires (Want).

## 1. Design System
**Typography:**
- English/Numbers: 'Jost' (Weights: 500 Medium, 700 Bold).
- Japanese: 'Zen Kaku Gothic New' (Weights: 400 Regular, 500 Medium).
- Look & Feel: Geometric, clean, editorial style.

**Color Palette:**
- Background (Body): #f4f7fa (Pale Ice)
- Background (Card/Panel): #ffffff (Pure White)
- Text (Main): #002B5B (Intellectual Navy)
- Must Accent: #004CBF (Royal Blue)
- Want Accent: #F1C40F (Active Gold)
- Border: #e2e8f0 (Cool Gray) - Used for separation instead of shadows.

**UI Rules:**
- Task Cards: Min-height 72px, Padding 16px/20px, Border-radius 8px.
- Sidebar: Fixed left, White background, Right border.
- Layout: 2-column Grid (Must/Want) with adjustable Ratio Slider.

## 2. Tech Stack
- Backend: Django 5.x, Python 3.x
- Frontend: HTML5, SCSS (Sass), Vanilla JS
- Database: SQLite (Dev)
- Libraries: SortableJS (DnD), FullCalendar (v6), Chart.js

## 3. Data Models
**Task Model:**
- title: CharField
- type: 'must' | 'want'
- due_date: Date (For Must deadline)
- execution_date: Date (For Want planned date)
- status: 'pending' | 'done' | 'dropped'
- sync_id: UUID (Links Must/Want tasks created together in "Both" mode)
- order: Float (For drag-and-drop sort)

## 4. Core Features & Pages
**P1: Home (/)**
- View: List View (Default).
- Layout: 2 Columns (Must/Want). Width adjusted by a Ratio Slider.
- Logic: Show tasks for "Today".
- UI: "Quick Add" bar at top.

**P2: Weekly (/weekly/)**
- View: Horizontal Scroll Board (7 Columns: Mon-Sun).
- Layout: Column width 300px fixed. Sticky date headers.
- Logic: Drag & drop tasks to reschedule dates.

**P3: Calendar (/calendar/)**
- View: FullCalendar (Month view).
- Design: Must events (Blue), Want events (Gold).
- Logic: Filter toggle for Must/Want.

**P4: Dashboard (/dashboard/)**
- View: KPI Cards + Charts.
- Content: "Today's Focus" (Donut), "Streak", "Must/Want Balance".
- Font: Use huge 'Jost' font for numbers.

## 5. Logic Requirements
- **Both Mode Creation:** When creating "Both", create 2 records (Must & Want) linked by `sync_id`.
- **Sync Delete:** If a synced task is deleted, ask to delete the pair.
- **Date Unification:** If Must date == Want date, create only 1 Must task.
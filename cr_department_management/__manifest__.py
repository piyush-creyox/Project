{
    "name": "Department Management",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Extra Tools",
    "summary": """
    	department management.
        """,
    "license": "OPL-1",
    "version": "18.0.0.0",
    "sequence":1,
    "description": """
     	department management.
        """,
    "depends": [
        "base","mail","sale"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/department_department.xml",
        "views/employee_employee.xml",
        "views/student_student.xml",
        "views/sale_order_line_views.xml",
        "wizard/split_sale_wiz_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}

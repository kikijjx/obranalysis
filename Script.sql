CREATE TABLE School_Kind_Table
(
	school_kind_id INTEGER PRIMARY KEY,
	school_kind_name TEXT
);

CREATE TABLE Schoole_Type_Table
(
	school_type_id INTEGER PRIMARY KEY,
	school_type_name TEXT
);

CREATE TABLE Area_Table
(
	area_id INTEGER PRIMARY KEY,
	area_name TEXT,
	township_name TEXT,
	government_if INTEGER,
	government_name TEXT
);

CREATE TABLE Town_Type_Table
(
	town_type_id INTEGER PRIMARY KEY,
	town_type_name TEXT
);

CREATE TABLE Subject_Table
(
	subject_id INTEGER PRIMARY KEY,
	subject_name TEXT
);

CREATE TABLE School_Table
(
	school_id TEXT PRIMARY KEY,
	school_CODE INTEGER,
	law_address TEXT,
	school_name TEXT,
	school_kind_id INTEGER,
	school_type_id INTEGER,
	area_id INTEGER,
	town_id INTEGER,
	FOREIGN KEY (school_kind_id) REFERENCES Scool_Kind_Table (school_kind_id),
	FOREIGN KEY (school_type_id) REFERENCES Scool_Type_Table (school_type_id),
	FOREIGN KEY (area_id) REFERENCES Area_Table (area_id),
	FOREIGN KEY (town_id) REFERENCES Town_Table (town_id)
);

CREATE TABLE School_Student_Table
(
	student_id TEXT PRIMARY KEY,
	school_code INTEGER ,
	class TEXT,
	FOREIGN KEY (school_code) REFERENCES School_Table (school_code)
);

CREATE TABLE Subject_Form_Table
(
	subject_form_id INTEGER PRIMARY KEY,
	subject_id INTEGER,
	year_of_exam INTEGER,
	A_tasks_count INTEGER,
	B_tasks_count INTEGER,
	C_tasks_count INTEGER,
	D_tasks_count INTEGER,
	FOREIGN KEY (subject_id) REFERENCES Subject_Table (subject_id)
);

CREATE TABLE Result_Table
(
	result_id INTEGER PRIMARY KEY,
	student_id TEXT,
	subject_form_id INTEGER,
	primary_score INTEGER,
	accuracy INTEGER CHECK(accuracy >= 0 and accuracy <= 100),
	score_100 INTEGER CHECK(score_100 >= 0 and score_100 <= 100),
	result_5 INTEGER CHECK(result_5 >= 2 and result_5 <= 5),
	FOREIGN KEY (student_id) REFERENCES School_Student_Table (student_id),
	FOREIGN KEY (subject_form_id) REFERENCES Subject_Form_Table (subject_form_id)
);

CREATE TABLE Task_Table
(
	task_id INTEGER PRIMARY KEY,
	result_id INTEGER,
	answer TEXT,
	FOREIGN KEY (result_id) REFERENCES Result_Table (result_id)
);
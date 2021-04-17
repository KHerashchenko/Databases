CREATE TABLE Location(
    LocationID SERIAL PRIMARY KEY,
    Regname varchar(128),
    AreaName varchar(128),
    TerName  varchar(128),
    TerTypeName varchar(128),
    CONSTRAINT location_unique_constraint UNIQUE (Regname, AreaName, TerName)
);

CREATE TABLE School(
    SchoolID SERIAL PRIMARY KEY,
    Name text,
    TypeName varchar(128) default NULL,
    Parent text default NULL,
    LocationID integer default NULL,
    CONSTRAINT school_unique_constraint UNIQUE (Name),
    CONSTRAINT school_location
        FOREIGN KEY(LocationID)
        REFERENCES Location (LocationID)
);


CREATE TABLE Student(
    OutID UUID PRIMARY KEY,
    Birth smallint,
    SexTypeName varchar(128),
    RegTypeName VARCHAR (128),
    ClassProfileName VARCHAR (128),
    ClassLangName VARCHAR (128),
    LocationID integer,
    SchoolID integer,
    CONSTRAINT student_location
        FOREIGN KEY(LocationID)
        REFERENCES Location (LocationID),
    CONSTRAINT student_school
        FOREIGN KEY(SchoolID)
        REFERENCES School (SchoolID)
);

CREATE TABLE Exam(
    ExamID SERIAL PRIMARY KEY,
    OutID uuid,
    Subject varchar(128),
    PTName TEXT,
    LocationID integer,
    Lang VARCHAR (128) default NULL,
    TestStatus VARCHAR (128),
    AdaptScale VARCHAR(128),
    Year smallint,
    Ball100 smallint,
    Ball12 smallint,
    Ball smallint,
    CONSTRAINT exam_location
        FOREIGN KEY(LocationID)
        REFERENCES Location (LocationID),
    CONSTRAINT exam_student
        FOREIGN KEY(OutID)
        REFERENCES Student (OutID)
)
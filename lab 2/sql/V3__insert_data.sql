INSERT INTO Location (Regname, AreaName, TerName, TerTypeName)
SELECT DISTINCT Regname, AreaName, TerName, TerTypeName FROM zno_results
ON CONFLICT DO NOTHING;

INSERT INTO Location (Regname, AreaName, TerName, TerTypeName)
SELECT DISTINCT EORegName, EOAreaName, EOTerName, null FROM zno_results
ON CONFLICT DO NOTHING;

INSERT INTO Location (Regname, AreaName, TerName, TerTypeName)
SELECT DISTINCT UkrPTRegName, UkrPTAreaName, UkrPTTerName, null FROM zno_results
ON CONFLICT DO NOTHING;

INSERT INTO Location (Regname, AreaName, TerName, TerTypeName)
SELECT DISTINCT HistPTRegName, HistPTAreaName, HistPTTerName, null FROM zno_results
ON CONFLICT DO NOTHING;

-- ---

INSERT INTO School (Name, TypeName, Parent, LocationID)
select distinct 
    EOName, EOTypeName, EOParent, LocationID
from zno_results zr
left join Location l on (zr.EORegName = l.RegName
                    AND zr.EOAreaName = l.AreaName
                    AND zr.EOTerName = l.TerName)
ON CONFLICT DO NOTHING;

-- ---

INSERT INTO Student 
SELECT distinct 
    OutID, Birth, SexTypeName, RegTypeName, ClassProfileName, ClassLangName, l.LocationID, SchoolID
from zno_results zr
left join Location l using (RegName, AreaName, TerName)
left join School s on (zr.EOName  = s.Name
                    AND zr.EOTypeName  = s.TypeName
                    AND zr.EOParent = s.Parent)
ON CONFLICT DO NOTHING;

-- ---

INSERT INTO Exam(OutID, Subject, PTName, LocationID, Lang, TestStatus, AdaptScale, Year, Ball100, Ball12, Ball)
select OutID, UkrTest, UkrPTName, l.LocationID, null, UkrTestStatus, UkrAdaptScale, Year, UkrBall100, UkrBall12, UkrBall
from zno_results zr
left join Student st using (OutID)
left join School s on (zr.EOName  = s.Name
                    AND zr.EOTypeName  = s.TypeName
                    AND zr.EOParent = s.Parent)
left join Location l on (zr.UkrPTRegName = l.RegName
                    AND zr.UkrPTAreaName = l.AreaName
                    AND zr.UkrPTTerName = l.TerName)
ON CONFLICT DO NOTHING;

-- ---

INSERT INTO Exam(OutID, Subject, PTName, LocationID, Lang, TestStatus, AdaptScale, Year, Ball100, Ball12, Ball)
select OutID, HistTest, HistPTName, l.LocationID, null, HistTestStatus, null, Year, HistBall100, HistBall12, HistBall
from zno_results zr
left join Student st using (OutID)
left join School s on (zr.EOName  = s.Name
                    AND zr.EOTypeName  = s.TypeName
                    AND zr.EOParent = s.Parent)
left join Location l on (zr.HistPTRegName = l.RegName
                    AND zr.HistPTAreaName = l.AreaName
                    AND zr.HistPTTerName = l.TerName)
ON CONFLICT DO NOTHING;

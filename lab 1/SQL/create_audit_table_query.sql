INSERT INTO audit VALUES ('DATA/Odata2020File_encoded_400000.csv','waiting',NULL) 
                ON CONFLICT (filename) DO NOTHING;
DROP TABLE IF EXISTS extract_loader_landing_zone;
CREATE TABLE extract_loader_landing_zone (
	file_index INTEGER,
	file_name TEXT,
	col_a TEXT DEFAULT NULL,
	col_b TEXT DEFAULT NULL,
	col_c TEXT DEFAULT NULL,
	col_d TEXT DEFAULT NULL,
	col_e TEXT DEFAULT NULL,
	col_f TEXT DEFAULT NULL,
	col_g TEXT DEFAULT NULL,
	col_h TEXT DEFAULT NULL,
	col_i TEXT DEFAULT NULL,
	col_j TEXT DEFAULT NULL,
	col_k TEXT DEFAULT NULL,
	col_l TEXT DEFAULT NULL,
	col_m TEXT DEFAULT NULL,
	col_n TEXT DEFAULT NULL,
	col_o TEXT DEFAULT NULL,
	col_p TEXT DEFAULT NULL,
	col_q TEXT DEFAULT NULL,
	col_r TEXT DEFAULT NULL,
	col_s TEXT DEFAULT NULL,
	col_t TEXT DEFAULT NULL,
	col_u TEXT DEFAULT NULL,
	col_v TEXT DEFAULT NULL,
	col_w TEXT DEFAULT NULL,
	col_x TEXT DEFAULT NULL,
	col_y TEXT DEFAULT NULL,
	col_z TEXT DEFAULT NULL,
	insert_time TIMESTAMP DEFAULT current_timestamp
);
SELECT * FROM extract_loader_landing_zone;

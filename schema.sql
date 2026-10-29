 -- جدول الالواح الشمسيه 
create table if not exists panels (
 ID SERIAL primary key ,
 brand VARCHAR (100) not null ,
 model VARCHAR (150) not null ,
 pmax numeric (6,2) Not null check (pmax > 0),
 voc numeric (5,2) not null check (voc > 0 ),
 isc numeric (5,2) not null check (isc > 0 ),
 vmp numeric (5,2) not null check ( vmp > 0 and vmp < voc ),
 imp numeric (5,2) not null check (imp > 0 and imp < isc ),
 temp_coeff_pmax numeric (5, 3) not null check (temp_coeff_pmax < 0 ),
 efficiency numeric (4, 2) not null check (efficiency > 0 and efficiency <= 100),
 length_mm INTEGER NOT NULL CHECK (length_mm > 0),
 width_mm INTEGER NOT NULL CHECK (width_mm > 0),

 created_at timestamptz default CURRENT_TIMESTAMP ,
CONSTRAINT uq_panel_brand_model unique (brand , model)
) ;
-- جدول الانفرتات 
create table if not exists inverters (
ID SERIAL primary key ,
brand VARCHAR (100) not null ,
model VARCHAR (150) not null ,
rated_ac_power NUMERIC(8, 2) NOT NULL CHECK (rated_ac_power > 0),
max_dc_voltage NUMERIC(6, 2) NOT NULL CHECK (max_dc_voltage > 0),
mppt_voltage_min NUMERIC(6, 2) NOT NULL CHECK (mppt_voltage_min > 0),
mppt_voltage_max NUMERIC(6, 2) NOT NULL CHECK (mppt_voltage_max > mppt_voltage_min),
max_dc_current NUMERIC(5, 2) NOT NULL CHECK (max_dc_current > 0),
mppt_tracks_count SMALLINT NOT NULL DEFAULT 1 CHECK (mppt_tracks_count > 0),
grid_phases SMALLINT NOT NULL CHECK (grid_phases IN (1, 3))

);
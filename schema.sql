CREATE TABLE all_stats(
	team_id INT PRIMARY KEY,
	total_first_downs TEXT,
	first_downs_rush_pass_penalty TEXT,
	third_down_conversions TEXT,
	fourth_down_conversions TEXT,
	total_offensive TEXT,
	offense_plays_avg TEXT,
	total_rushing TEXT,
	rushing_plays_avg TEXT,
	total_passing TEXT,
	passing_comp_att_int_avg TEXT,
	sacks TEXT,
	field_goals TEXT,
	touchdowns TEXT,
	touchdowns_rush_pass_returns_def TEXT,
	avg_possesion TEXT,
	turnover_ratio TEXT
);

CREATE TABLE allowed_all_stats(
	team_id INT PRIMARY KEY,
	allowed_total_first_downs TEXT,
	allowed_first_downs_rush_pass_penalty TEXT,
	allowed_third_down_conversions TEXT,
	allowed_fourth_down_conversions TEXT,
	allowed_total_offensive TEXT,
	allowed_offense_plays_avg TEXT,
	allowed_total_rushing TEXT,
	allowed_rushing_plays_avg TEXT,
	allowed_total_passing TEXT,
	allowed_passing_comp_att_int_avg TEXT,
	allowed_sacks TEXT,
	allowed_field_goals TEXT,
	allowed_touchdowns TEXT,
	allowed_touchdowns_rush_pass_returns_def TEXT,
	allowed_avg_possesion TEXT,
	allowed_turnover_ratio TEXT
);

CREATE TABLE teams(
    team_id INT PRIMARY KEY,
    team_name TEXT
);

CREATE TABLE rankings(
	team_id INT PRIMARY KEY,
	ranking INT NOT NULL,
	record TEXT
);
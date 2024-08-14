
CREATE TABLE IF NOT EXISTS users
(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR (255) NOT NULL,
    email VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS talked_time
(
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(50) NOT NULL,
    user_id INT REFERENCES users(user_id),
    duration INT,
    timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS speaker_used
(
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(50) NOT NULL,
    user_id INT REFERENCES users(user_id),
    speaker_amount INT DEFAULT 1,
    speaker_type VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS voice_sentiment
(
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(50) NOT NULL,
    user_id INT REFERENCES users(user_id),
    sentiment VARCHAR(50) DEFAULT 'Neutral'
);
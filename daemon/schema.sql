-- Table: skype_net_send

-- DROP TABLE skype_net_send;

CREATE TABLE skype_net_send
(
  id serial NOT NULL,
  "to" character varying(120),
  message text,
  send boolean DEFAULT false,
  CONSTRAINT skype_net_send_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE skype_net_send
  OWNER TO web_script;
COMMENT ON TABLE skype_net_send
  IS 'Проект "Скайп-Секретарь" очередь сообщений на отправку';


-- Table: skype_messages

-- DROP TABLE skype_messages;

CREATE TABLE skype_messages
(
  id serial NOT NULL,
  skype_id integer,
  status character varying(30),
  "from" character varying(120),
  body text,
  message_date timestamp without time zone,
  chat_name character varying(120),
  CONSTRAINT skype_messages_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE skype_messages
  OWNER TO web_script;
COMMENT ON TABLE skype_messages
  IS 'Проект "Скайп-Секретарь" хранилище входящих сообщений';

-- Index: skype_messages_from_idx

-- DROP INDEX skype_messages_from_idx;

CREATE INDEX skype_messages_from_idx
  ON skype_messages
  USING btree
  ("from" COLLATE pg_catalog."default");

-- Index: skype_messages_status_idx

-- DROP INDEX skype_messages_status_idx;

CREATE INDEX skype_messages_status_idx
  ON skype_messages
  USING btree
  (status COLLATE pg_catalog."default");


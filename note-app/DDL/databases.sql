drop table if exists notes;

create table notes (
    id primary key comment 'ID',
    title text not null comment 'ノートのタイトル',
    content_url text not null comment "マークダウンの内容が書かれているファイルのURL",
    user_id int comment 'いずれ追加したいログイン機能',
    created_at datetime not null comment '作成日時',
    updated_at datetime comment '更新日時',
)
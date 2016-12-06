DROP DATABASE IF EXISTS `wiki`;
CREATE DATABASE IF NOT EXISTS `wiki`;
USE `wiki`;
CREATE TABLE user (
  user_id INT          NOT NULL AUTO_INCREMENT,
  account VARCHAR(150) NOT NULL,
  pwd     VARCHAR(25)  NOT NULL,
  avatar  VARCHAR(250) NOT NULL, /* 头像对应的url */
  PRIMARY KEY (account)
);
CREATE TABLE template (
  template_id INT          NOT NULL  AUTO_INCREMENT,
  type        VARCHAR(250) NOT NULL, /* 模板名字 */
  PRIMARY KEY (type)
);
CREATE TABLE wiki (
  wiki_id   INT          NOT NULL AUTO_INCREMENT,
  user_id   INT          NOT NULL, /*  创建者ID  */
  name      VARCHAR(150) NOT NULL, /*  词条名字  */
  content   TEXT         NOT NULL, /*  词条内容  */
  type      VARCHAR(250) NOT NULL, /*  模板类型  */
  visit_cnt INT          NOT NULL, /*  访问量   */
  status    INT          NOT NULL DEFAULT 0, /* 1 表示通过, 0 表示正在审核, -1 表示审核失败 */
  PRIMARY KEY (wiki_id, user_id)
);
CREATE TABLE wiki_pic (
  wiki_id INT NOT NULL,
  pic_url VARCHAR(250),
  PRIMARY KEY (wiki_id)
);
CREATE TABLE discussion (
  dis_id  INT NOT NULL AUTO_INCREMENT,
  wiki_id INT NOT NULL,
  user_id INT NOT NULL,
  content INT NOT NULL,
  PRIMARY KEY (dis_id)
);
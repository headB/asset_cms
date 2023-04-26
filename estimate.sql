/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.121.66
 Source Server Type    : MySQL
 Source Server Version : 50651 (5.6.51)
 Source Host           : 192.168.121.66:3307
 Source Schema         : estimate

 Target Server Type    : MySQL
 Target Server Version : 50651 (5.6.51)
 File Encoding         : 65001

 Date: 26/04/2023 14:08:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (19, 'Can add admin', 7, 'add_admin');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (20, 'Can change admin', 7, 'change_admin');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (21, 'Can delete admin', 7, 'delete_admin');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (22, 'Can add class room', 8, 'add_classroom');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (23, 'Can change class room', 8, 'change_classroom');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (24, 'Can delete class room', 8, 'delete_classroom');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (25, 'Can add port type', 9, 'add_porttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (26, 'Can change port type', 9, 'change_porttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (27, 'Can delete port type', 9, 'delete_porttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (28, 'Can add subject detail', 10, 'add_subjectdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (29, 'Can change subject detail', 10, 'change_subjectdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (30, 'Can delete subject detail', 10, 'delete_subjectdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (31, 'Can add estimate history', 11, 'add_estimatehistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (32, 'Can change estimate history', 11, 'change_estimatehistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (33, 'Can delete estimate history', 11, 'delete_estimatehistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (34, 'Can add location', 12, 'add_location');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (35, 'Can change location', 12, 'change_location');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (36, 'Can delete location', 12, 'delete_location');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (37, 'Can add front end show', 13, 'add_frontendshow');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (38, 'Can change front end show', 13, 'change_frontendshow');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (39, 'Can delete front end show', 13, 'delete_frontendshow');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (1, 'pbkdf2_sha256$100000$J3LlHTmY4sjC$Cf7szE29KE6X119TjZRRkPhoQo/ZBCsC09V7gKKdprc=', '2018-10-24 06:16:11.151633', 1, 'admin', '', '', '775121173@qq.com', 1, 1, '2018-07-08 07:24:27.259411');
COMMIT;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (1, '2018-10-24 07:17:53.553624', '5', 'Admin object (5)', 2, '[{\"changed\": {\"fields\": [\"reset_videocode_request\"]}}]', 7, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (2, '2018-10-24 07:20:27.048019', '5', 'Admin object (5)', 2, '[{\"changed\": {\"fields\": [\"reset_videocode_request\"]}}]', 7, 1);
COMMIT;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'login', 'admin');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'login', 'classroom');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'login', 'estimatehistory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'login', 'frontendshow');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'login', 'location');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'login', 'porttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'login', 'subjectdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'contenttypes', '0001_initial', '2018-07-08 07:23:52.297038');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'auth', '0001_initial', '2018-07-08 07:23:54.092425');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'admin', '0001_initial', '2018-07-08 07:23:54.489856');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-07-08 07:23:54.520882');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2018-07-08 07:23:54.763357');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2018-07-08 07:23:54.923243');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'auth', '0003_alter_user_email_max_length', '2018-07-08 07:23:55.084491');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'auth', '0004_alter_user_username_opts', '2018-07-08 07:23:55.097455');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'auth', '0005_alter_user_last_login_null', '2018-07-08 07:23:55.227543');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'auth', '0006_require_contenttypes_0002', '2018-07-08 07:23:55.236318');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2018-07-08 07:23:55.250730');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'auth', '0008_alter_user_username_max_length', '2018-07-08 07:23:55.405237');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'auth', '0009_alter_user_last_name_max_length', '2018-07-08 07:23:55.567591');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'sessions', '0001_initial', '2018-07-08 07:23:55.687110');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'login', '0001_initial', '2018-07-08 07:27:48.187236');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('0011sv4zi0rv86y69gbyodao84fhpzi3', 'YjZjYzhjZGQ2YWY5M2ZjODczMjhjZWJjYjRkMTg0MDAwYTBkYWUyMDp7InZlcmlmeWNvZGUiOiIxVlhaIn0=', '2019-11-08 12:47:22.949621');
COMMIT;

-- ----------------------------
-- Table structure for login_admin
-- ----------------------------
DROP TABLE IF EXISTS `login_admin`;
CREATE TABLE `login_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `password` varchar(200) NOT NULL,
  `department` int(11) NOT NULL DEFAULT '20',
  `email` varchar(100) DEFAULT NULL,
  `realname` varchar(50) NOT NULL,
  `last_login_time` datetime(6) DEFAULT NULL,
  `last_login_ip` varchar(50) DEFAULT NULL,
  `weixin_openid` varchar(80) DEFAULT NULL,
  `weixin_openid_tmp` varchar(81) DEFAULT NULL,
  `xcx_openid` varchar(101) DEFAULT NULL,
  `xcx_openid_tmp` varchar(101) DEFAULT NULL,
  `reset_videocode_request` varchar(200) DEFAULT NULL,
  `quick_verify` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_admin
-- ----------------------------
BEGIN;
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (5, 'kuman', 'd809751ea2cac6d68813e5f203759fcf', 1, 'lizhixuan@wolfcode.cn', '黎智煊', '2023-04-26 02:30:14.000000', '192.168.10.35', 'obzD1vx3sXEWxtb3Izz_MnSe_hGY', NULL, 'o_wpd5eqWy6VicAGDRlAGsDMT0T4', NULL, NULL, '6119');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (6, '冯文锦', '7973254babe378a6b286d117428a3a12', 1, 'fengwenjin@520it.com', '冯文锦', '2019-08-02 14:06:23.000000', '192.168.113.15', 'obzD1vxIQEC0LA9Mp4cv9t90UTi4', NULL, 'o_wpd5X91UkWiH8PS29Ea4BGXQbU', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (9, '陈阳', '35ec044f9b2ec3528a7f17ef4b44adc6', 32, 'chenyang@wolfcode.cn', '陈阳', '2020-11-13 09:22:06.000000', '192.168.113.15', 'obzD1vxaxgEDpoTcrw5UTSleiISc', NULL, 'o_wpd5bFAMWtdlo_IzQDwk-w5Q6A', NULL, NULL, '07-15 13:15');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (11, 'will', 'b6f23860ebb1cf0963543122cf5c8987', 27, 'renxiaolong@520it.com', '任小龙', '2018-05-28 09:19:09.000000', '', '', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (13, '吴嘉俊', '0bfb0093093550bbf97168cefa14fac2', 27, 'wujiajun@wolfcode.cn', '吴嘉俊', '2018-05-28 09:19:09.000000', '', '', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (14, '李红梅', '3305c52882e4c29a8329ecea28ac2927', 27, 'lihongmei@wolfcode.cn', '李红梅', '2019-03-14 03:03:10.000000', '192.168.113.15', '', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (15, '王一萍', '89739dc2aade2a63334be93caa039f9d', 1, 'wangyiping1@wolfcode.cn', '王一萍', '2020-07-15 07:31:42.000000', '192.168.113.15', '', NULL, 'o_wpd5UZc7gZ0QLieR2FJQs70Hos', NULL, NULL, '11-27 12:48');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (16, 'sunyanling', 'c4c254d762f0d66bc4a8975871ac9a7f', 20, 'sunyanling@wolfcode.cn', '孙燕玲', '2020-10-18 02:30:32.000000', '192.168.113.15', '', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (17, '何细妹', 'a396f3ea66f82f41a0b22bcd97cbf4e4', 20, 'heximei@wolfcode.cn', '何细妹', '2020-11-03 10:34:26.000000', '192.168.113.15', '', NULL, 'o_wpd5Xi_uzsZIMkyBnb8JtMhF3E', 'o_wpd5Xi_uzsZIMkyBnb8JtMhF3E', NULL, '12-24 18:56');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (20, 'Miki', '1f1f94635e01b308f4d618934c9cc9e5', 30, 'oushuiping@520it.com', '欧水萍', '2018-09-18 06:11:00.000000', '192.168.113.15', 'obzD1v8EWRngO56uLMt7PGPiPuHY', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (21, '闫乐', 'a6fd5566a1decc405a919a97fa57b74e', 27, 'yanle@wolfcode.cn', '闫乐', NULL, NULL, '', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (25, '谢秋纯', 'f5837897def1fb8e562e45bfe714a35d', 27, 'xieqiuchun@wolfcode.cn', '谢秋纯', '2021-03-31 06:48:09.000000', '172.17.0.2', 'obzD1v6NI__eCB8vqBkmuLRX1v3g', NULL, 'o_wpd5c6Oj_l4sdWNL6jgrNn6D1E', 'o_wpd5c6Oj_l4sdWNL6jgrNn6D1E', NULL, '12-06 10:52');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (28, 'xiejinling', 'e4dc6fc7d382adf3f7a1d48e10e200d0', 20, 'xiejinling@wolfcode.cn', '谢金玲', '2019-11-27 02:52:56.000000', '192.168.113.15', 'obzD1v4EoyB0pBioIDMY1_fYX5rI', NULL, 'o_wpd5d718aLQpHVgzkhRCehqHXM', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (32, 'obzD1v5xIOMUXl1xjIDZX1lYJ5e4', '6666', 20, 'lizhiwei@wolfcode.cn', '李志伟', NULL, NULL, 'obzD1v5xIOMUXl1xjIDZX1lYJ5e4', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (33, 'obzD1v5Be8IW9Ii4o2tBmZtOftvg', '6666', 20, 'chenhui@wolfcode.cn', '陈惠', '2019-09-04 15:36:34.000000', '192.168.113.15', 'obzD1v5Be8IW9Ii4o2tBmZtOftvg', NULL, 'o_wpd5bMuUDeR4qiiblM0VbO-DII', NULL, NULL, '0100');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (34, 'obzD1v6h1rxq10ZLcut_fQ60cEp0', '6666', 20, 'yanglong@wolfcode.cn', '杨龙', '2019-06-06 00:59:56.000000', '192.168.113.15', 'obzD1v6h1rxq10ZLcut_fQ60cEp0', NULL, 'o_wpd5apsu3NknYc3rhTFbPAbWpY', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (35, 'obzD1v6iNUrB8589EkZqkXPPGM5Y', '6666', 20, 'kongweisheng@wolfcode.cn', '孔伟胜', NULL, NULL, 'obzD1v6iNUrB8589EkZqkXPPGM5Y', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (36, 'obzD1v_zRcnsU5CcayMGe2vZuCO8', '6666', 20, 'wenyanjun@520it.com', '温艳军', '2018-09-30 07:13:43.000000', '192.168.113.15', 'obzD1v_zRcnsU5CcayMGe2vZuCO8', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (72, 'obzD1v6f2X15dlmlkAUZML29cqwI', '6666', 20, 'xxx@wolfcode.cn', '基基', '2020-03-05 01:41:25.000000', '192.168.113.15', 'obzD1v6f2X15dlmlkAUZML29cqwI', NULL, 'o_wpd5Yzs_xkJWhshPdt3M8S9Oj8', NULL, NULL, '11-13 23:26');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (74, 'obzD1vwkzyAJtz_H9_Bva1vACvpA', '6666', 20, 'xxx@wolfcode.cn', 'fanjialong', NULL, NULL, 'obzD1vwkzyAJtz_H9_Bva1vACvpA', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (75, 'obzD1v62d7OdGe0zf-n1tu4n4bcI', '6666', 20, 'xxx@wolfcode.cn', '陈志伟', '2018-11-27 05:25:26.000000', '192.168.113.15', 'obzD1v62d7OdGe0zf-n1tu4n4bcI', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (76, 'obzD1vws3aX1p5mNNjiGPsX9PApM', '6666', 20, 'huangshuwei@wolfcode.cn', '黄树伟', '2018-11-21 04:07:27.000000', '192.168.113.15', 'obzD1vws3aX1p5mNNjiGPsX9PApM', NULL, 'o_wpd5QZ2ockBP6hvb501-UyKDNs', NULL, NULL, '9629');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (106, 'o_wpd5fKHonpBPpK49o4ZqvNdosc', '6666', 20, 'zhaoyanming@wolfcode.cn', 'wolfcode', '2019-09-07 10:44:12.000000', '192.168.113.15', NULL, NULL, 'o_wpd5fKHonpBPpK49o4ZqvNdosc', NULL, NULL, '8820');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (113, 'o_wpd5WcoVTCkaqPsiSbUf6YFLZ0', '6666', 20, 'liangshunyong@wolfcode.cn', 'wolfcode', '2020-01-12 04:51:53.000000', '192.168.113.15', NULL, NULL, 'o_wpd5WcoVTCkaqPsiSbUf6YFLZ0', NULL, NULL, '1594');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (114, 'o_wpd5Yb1MqJ-Nl4Er6MJa_0oCCo', '6666', 20, 'xxx@wolfcode.cn', '黄海燕', '2019-05-31 12:44:48.000000', '192.168.113.15', NULL, NULL, 'o_wpd5Yb1MqJ-Nl4Er6MJa_0oCCo', NULL, NULL, '11-27 10:34');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (115, 'o_wpd5QRDAYCRCT4VTcHggGDy9rg', '6666', 20, 'xxx@wolfcode.cn', '郑琪', '2019-03-28 01:12:45.000000', '192.168.113.15', NULL, NULL, 'o_wpd5QRDAYCRCT4VTcHggGDy9rg', NULL, NULL, '11-27 12:31');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (116, 'o_wpd5eHcR82YRUiCTZh-mAM7u4I', '6666', 20, 'cuixingxing@wolfcode.cn', 'wolfcode', '2019-05-22 01:17:15.000000', '192.168.113.15', NULL, NULL, 'o_wpd5eHcR82YRUiCTZh-mAM7u4I', NULL, NULL, '0376');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (117, 'o_wpd5fShBYqhWkVkiTJhYpqjtrA', '6666', 20, 'zhongxinling@wolfcode.cn', 'wolfcode', '2020-12-01 04:25:36.000000', '172.17.0.2', NULL, NULL, 'o_wpd5fShBYqhWkVkiTJhYpqjtrA', NULL, NULL, '2805');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (118, 'o_wpd5ZvokIXdMfDPUA7ikmp4xWE', '6666', 20, 'xxx@wolfcode.cn', '范佳龙', '2018-11-27 05:03:41.000000', '192.168.113.15', NULL, NULL, 'o_wpd5ZvokIXdMfDPUA7ikmp4xWE', NULL, NULL, '11-27 13:01');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (119, 'o_wpd5biUN0cHrtgpt7by5t44v3E', '6666', 1, 'will@wolfcode.cn', 'wolfcode', '2020-03-06 02:22:04.000000', '192.168.113.15', NULL, NULL, 'o_wpd5biUN0cHrtgpt7by5t44v3E', NULL, NULL, '4557');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (120, 'o_wpd5Tu3IyLBZMEHPfQvKt8QSxM', '6666', 20, 'xxx@wolfcode.cn', '陈刚', '2018-12-13 00:29:04.000000', '192.168.113.15', NULL, NULL, 'o_wpd5Tu3IyLBZMEHPfQvKt8QSxM', NULL, NULL, '11-27 17:27');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (121, 'o_wpd5ahhZ4tANTBjgY4Bl2dXpEU', '6666', 20, 'xxx@wolfcode.cn', '孔维胜', '2019-01-02 08:17:04.000000', '192.168.113.15', NULL, NULL, 'o_wpd5ahhZ4tANTBjgY4Bl2dXpEU', NULL, NULL, '11-29 10:04');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (122, 'o_wpd5bRAy44wkExbuEsqul6HUoA', '6666', 20, 'xxx@wolfcode.cn', '冷光艳', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12-18 09:20');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (123, 'qiucuiya', '0dcb5f10d0467c9e2acd07fa76601747', 20, 'qiucuiya@wolfcode.cn', '丘翠雅', '2019-08-30 10:48:09.000000', '192.168.113.15', NULL, NULL, 'o_wpd5YSoxnFdfaC3xOop3vWIusE', 'o_wpd5eEdvSXp3FfY2bjpieVFJtc', NULL, '07-20 11:45');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (124, 'o_wpd5cmAwdukYTs_TCjAgjnG_Js', '6666', 20, 'xxx@wolfcode.cn', '刘显俊', '2021-09-15 14:54:03.000000', '172.17.0.2', NULL, NULL, 'o_wpd5cmAwdukYTs_TCjAgjnG_Js', NULL, NULL, '01-24 15:11');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (125, '何金坪', '2dd1c2afdaf7f0cb94a34d6404bd4209', 20, 'hejinping@wolfcode.cn', '何金坪', '2019-09-08 06:31:30.000000', '192.168.7.143', 'obzD1v5GbS2LD6Q8SmBxD2egaGEI', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (126, 'o_wpd5eFdwg7j1zH7LPfNlcVZuEY', '6666', 20, 'xxx@wolfcode.cn', '刘俊飞', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '03-29 15:19');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (127, 'o_wpd5UOQA4rVASYGxZ1aE6UhOc0', '6666', 20, 'xxx@wolfcode.cn', '刘晓琪', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '03-30 12:12');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (128, '潘小雅', 'd122e1f8be6041e657a33a82f9e5a3c3', 20, 'panxiaoya@wolfcode.cn', '潘小雅', '2019-11-21 02:04:52.000000', '192.168.113.15', NULL, NULL, 'o_wpd5XxS5Pv9ZVitXG_TrRDc2BM', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (129, 'o_wpd5XxS5Pv9ZVitXG_TrRDc2BM', '6666', 20, 'xxx@wolfcode.cn', '潘小雅', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '04-29 17:50');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (130, 'o_wpd5Zwi9tORuWvn0L6XXdqETms_1', '6666', 20, 'xxx@wolfcode.cn', '袁丽霞', NULL, NULL, NULL, NULL, 'o_wpd5Zwi9tORuWvn0L6XXdqETms_1', NULL, NULL, '05-06 10:29');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (131, '袁丽霞', 'c81ec6b5a0dd54b8a667a778d000f632', 20, 'yuanlixia@wolfcode.cn', '袁丽霞', '2020-01-13 10:38:03.000000', '192.168.113.15', NULL, NULL, 'o_wpd5Zwi9tORuWvn0L6XXdqETms', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (132, 'huangshaocun', 'b65bd772c3b0dfebf0a189efd420352d', 20, 'huangshaocun@wolfcode.cn', '黄少存', '2022-09-23 11:07:11.000000', '172.17.0.2', NULL, NULL, 'o_wpd5T4l7bCtwhBkkJezKIwlCiw', NULL, NULL, '4662');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (133, 'o_wpd5RNB3WteziliS6WbSqhzr1Y', '6666', 20, 'weizhiwei@wolfcode.cn', 'wolfcode', '2019-12-04 08:21:52.000000', '192.168.113.15', NULL, NULL, 'o_wpd5RNB3WteziliS6WbSqhzr1Y', NULL, NULL, '8895');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (134, 'o_wpd5RX-xrXmDFjBLLcfkOusRQ4', '6666', 20, 'yaoyao@wolfcode.cn', 'wolfcode', '2020-07-06 06:27:13.000000', '192.168.113.15', NULL, NULL, 'o_wpd5RX-xrXmDFjBLLcfkOusRQ4', NULL, NULL, '1002');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (135, '何垚', '08b6403d608f51ed3fc74eff4c374f9a', 20, 'heyao@wolfcode.cn', '何垚', '2020-01-13 08:19:45.000000', '192.168.113.15', NULL, NULL, 'o_wpd5TE8zUSYbU_vJ9k77TU2o4k', NULL, NULL, '7356');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (136, 'o_wpd5aT3tyqviQ1QPQ9P8dDtYQA', '6666', 20, 'zhaowenxian@wolfcode.cn', 'wolfcode', '2020-08-24 15:27:26.000000', '192.168.113.15', NULL, NULL, 'o_wpd5aT3tyqviQ1QPQ9P8dDtYQA', NULL, NULL, '5852');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (137, 'o_wpd5YH6D3y00AdDb6Wz06k_A-g', '6666', 20, 'xxx@wolfcode.cn', '李敏', '2019-11-06 11:32:31.000000', '192.168.113.15', NULL, NULL, 'o_wpd5YH6D3y00AdDb6Wz06k_A-g', NULL, NULL, '07-10 13:11');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (138, 'o_wpd5bumw0dVancvCrZSXbPeEpA', '6666', 20, 'xxx@wolfcode.cn', '邱晓梅', NULL, NULL, NULL, NULL, NULL, 'o_wpd5bumw0dVancvCrZSXbPeEpA', NULL, '07-25 09:48');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (139, 'o_wpd5UVJ65jUmh2H7ppZ66iuSt0', '6666', 20, 'xxx@wolfcode.cn', '邓杨昆', NULL, NULL, NULL, NULL, NULL, 'o_wpd5UVJ65jUmh2H7ppZ66iuSt0', NULL, '07-31 15:05');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (140, 'chenyanling', 'c6ab182968072aadedd649bc6e97c666', 20, 'chenyanling@wolfcode.cn', '陈燕玲', '2019-12-01 08:22:53.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (142, 'sunyanling1', 'c4c254d762f0d66bc4a8975871ac9a7f', 20, 'sunyanling@wolfcode.cn', '孙燕玲', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (143, 'liuxiaoqi', '670b14728ad9902aecba32e22fa4f6bd', 20, 'liuxiaoqi@wolfcode.cn', '刘小奇', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (144, 'xiaoqiliu', '66ed3da3a111d2031f141540e785a108', 20, 'xiaoqiliu@wolfcode.cn', '刘晓琪', '2020-01-12 01:33:31.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (145, 'yangmiaoxia', '670b14728ad9902aecba32e22fa4f6bd', 20, 'yangmiaoxia@wolfcode.cn', '杨妙霞', '2021-04-02 08:19:30.000000', '172.17.0.2', NULL, NULL, 'o_wpd5fsAZ-00bK45YsXKCN3GxxU', NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (146, '胡红霞', '22dc092ccd45bfbeeee927abbf2b3617', 20, 'huhongxia@wolfcode.cn', '胡红霞', '2020-09-15 02:05:45.000000', '192.168.113.15', 'obzD1v932syTLhqJMdG3xGKmOiVc', NULL, 'o_wpd5d6uk5vHJkz9yPXB7JmC6oo', NULL, NULL, '1981');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (147, 'o_wpd5dKeEo0ZGN3DFTKz30JeYtg', '6666', 20, 'xxx@wolfcode.cn', '舒醒', NULL, NULL, NULL, NULL, NULL, 'o_wpd5dKeEo0ZGN3DFTKz30JeYtg', NULL, '10-15 12:08');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (148, 'wangxiaoxin', '01a9317d499d2751fcf880e408317236', 20, 'wangxiaoxin@wolfcode.cn', '王晓欣', '2021-01-25 01:19:28.000000', '172.17.0.2', NULL, NULL, 'o_wpd5enEt7YDGbA1bZhpuf3YQWk', NULL, NULL, '3315');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (151, 'o_wpd5bRb2iqcMhwWDDJzJjxO2fM', '6666', 20, 'liaobinhui@wolfcode.cn', '廖彬辉', '2022-05-21 12:10:42.000000', '172.17.0.2', NULL, NULL, 'o_wpd5bRb2iqcMhwWDDJzJjxO2fM', NULL, NULL, '5910');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (152, 'zhangdujuan', 'a95a26bfc37daed59aa861ae990ad748', 20, 'zhangdujuan@wolfcode.cn', '张杜鹃', '2020-10-14 03:38:57.000000', '192.168.113.15', NULL, NULL, 'o_wpd5Y-8ZBs-cQ75PBND1m7gCrE', NULL, NULL, '8402');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (153, 'mochou', '2c4a891f68bf42abcc6518143d198cc9', 20, 'mochou@wolfcode.cn', '莫愁', '2020-03-29 08:40:25.000000', '192.168.113.15', NULL, NULL, NULL, 'o_wpd5dngpFTgcvswWypQFMZbQUQ', NULL, '12-18 18:50');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (154, 'o_wpd5XybzcUI4lek5h4651Q8PSg', '6666', 20, 'limingsheng@wolfcode.cn', '李明胜', '2021-07-22 01:42:16.000000', '172.17.0.2', NULL, NULL, 'o_wpd5XybzcUI4lek5h4651Q8PSg', '', NULL, '11-20 10:15');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (155, 'songshanshan', '9cadcecbbe0cbcb47fc4ea221daf8345', 1, 'songshanshan@wolfcode.cn', '宋珊珊', '2020-03-10 09:21:28.000000', '192.168.113.15', NULL, NULL, 'o_wpd5X6M4IElzxD2HtFRpX6WeJs', NULL, NULL, '11-21 10:54');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (156, 'o_wpd5W07wFq5GtkoyJRLpRvxD10', '6666', 20, 'gaofangfang@wolfcode.cn', '高方方', '2020-01-13 01:28:38.000000', '192.168.113.15', NULL, NULL, 'o_wpd5W07wFq5GtkoyJRLpRvxD10', NULL, NULL, '11-22 11:31');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (157, 'o_wpd5ZYpfsVGPCypLrFcrKDBAX4', '6666', 20, 'xxx@wolfcode.cn', 'JUN', '2020-01-07 02:12:06.000000', '192.168.113.15', NULL, NULL, 'o_wpd5ZYpfsVGPCypLrFcrKDBAX4', NULL, NULL, '01-07 10:11');
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (158, 'yangxiulian', 'e941358ee929960202cc08c954b3e038', 20, 'yangxiulian@wolfcode.cn', '杨秀莲', '2020-11-05 02:19:58.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (159, '郑敏一', 'c2d8fdcf11f9e43039e75587a6a4c6de', 20, 'zhengminyi@wolfcode.cn', '郑敏一', '2020-03-28 02:26:35.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (160, 'maxiaosi', 'd273f8ef60f065ddafc5d1701a9ab303', 20, 'maxiaosi@wolfcode.cn', 'xx', '2020-05-30 01:11:32.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (161, '蔡文亿', '2651bf08e0d71b4ce9d3cd25299299bd', 20, 'caiwenyi@wolfcode.cn', 'xx', '2020-11-06 02:22:18.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (162, 'lilin', '4a3fe4b64d06363d4300d304065a526f', 20, 'lilin@wolfcode.cn', 'xx', '2020-06-14 14:01:15.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (164, 'maitingting', '25beef9dcc368f10208b50df1095ce57', 20, 'maitingting@wolfcode.cn', 'xx', '2020-11-08 03:29:42.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (168, 'huangqiong', '8ffab18a159ee9a84d0e5ca02b79c2e0', 20, 'huangqiong@wolfcode.cn', '黄琼', '2020-10-17 03:26:00.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (172, 'Dingye422422', '9a9e7937819be72c880cd124af8d4da1', 20, 'dingye@wolfcode.cn', 'xx', '2020-11-07 12:36:18.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (173, 'moxinyi', '11dc7c1823763e750d9073b4b609e483', 20, 'moxinyi@wolfcode.cn', '莫心怡', '2020-09-29 06:13:47.000000', '192.168.113.15', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `login_admin` (`id`, `username`, `password`, `department`, `email`, `realname`, `last_login_time`, `last_login_ip`, `weixin_openid`, `weixin_openid_tmp`, `xcx_openid`, `xcx_openid_tmp`, `reset_videocode_request`, `quick_verify`) VALUES (174, 'o_wpd5bZs7qnqY2YL0rrqHGzgz0w', '6666', 20, 'xxx@wolfcode.cn', '熊长青', '2023-04-11 07:00:23.000000', '172.17.0.1', NULL, NULL, 'o_wpd5bZs7qnqY2YL0rrqHGzgz0w', 'o_wpd5bZs7qnqY2YL0rrqHGzgz0w', NULL, '04-02 12:39');
COMMIT;

-- ----------------------------
-- Table structure for login_classroom
-- ----------------------------
DROP TABLE IF EXISTS `login_classroom`;
CREATE TABLE `login_classroom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` varchar(10) NOT NULL,
  `block_number` int(11) NOT NULL,
  `ip_addr` varchar(80) NOT NULL,
  `ACL` varchar(20) NOT NULL,
  `interface_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_classroom
-- ----------------------------
BEGIN;
INSERT INTO `login_classroom` (`id`, `class_number`, `block_number`, `ip_addr`, `ACL`, `interface_id`) VALUES (23, '课室1', 2, '31', '3343', 0);
INSERT INTO `login_classroom` (`id`, `class_number`, `block_number`, `ip_addr`, `ACL`, `interface_id`) VALUES (24, '课室2', 2, '32', '3339', 1);
INSERT INTO `login_classroom` (`id`, `class_number`, `block_number`, `ip_addr`, `ACL`, `interface_id`) VALUES (25, '课室3', 2, '33', '3340', 2);
COMMIT;

-- ----------------------------
-- Table structure for login_estimatehistory
-- ----------------------------
DROP TABLE IF EXISTS `login_estimatehistory`;
CREATE TABLE `login_estimatehistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `who` varchar(20) NOT NULL,
  `who_id` int(11) NOT NULL,
  `port` int(11) NOT NULL,
  `type_detail` int(11) NOT NULL,
  `setting_time` datetime(6) NOT NULL,
  `expired_time` datetime(6) NOT NULL,
  `class_info_id` varchar(200) NOT NULL,
  `class_room_name` varchar(100) NOT NULL,
  `teacher_name` varchar(100) NOT NULL,
  `class_name` varchar(100) NOT NULL,
  `total` varchar(20) NOT NULL,
  `is_stop` tinyint(1) NOT NULL,
  `send_email` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_estimatehistory
-- ----------------------------
BEGIN;
INSERT INTO `login_estimatehistory` (`id`, `sid`, `who`, `who_id`, `port`, `type_detail`, `setting_time`, `expired_time`, `class_info_id`, `class_room_name`, `teacher_name`, `class_name`, `total`, `is_stop`, `send_email`) VALUES (1007, 3, 'kuman', 5, 8082, 11, '2023-04-12 08:45:23.000000', '2023-04-12 10:45:23.000000', '5cfb3550-d90e-11ed-9b19-b7d2f01563ca', '25', '测试的名字', '测试的班级', '100', 1, 0);
INSERT INTO `login_estimatehistory` (`id`, `sid`, `who`, `who_id`, `port`, `type_detail`, `setting_time`, `expired_time`, `class_info_id`, `class_room_name`, `teacher_name`, `class_name`, `total`, `is_stop`, `send_email`) VALUES (1008, 5, 'kuman', 5, 8083, 12, '2023-04-13 10:34:45.000000', '2023-04-13 12:34:45.000000', 'cf00b930-d9e6-11ed-bbca-b9fa913eea04', '23', '小明', '华为ICT2021', '50', 1, 0);
INSERT INTO `login_estimatehistory` (`id`, `sid`, `who`, `who_id`, `port`, `type_detail`, `setting_time`, `expired_time`, `class_info_id`, `class_room_name`, `teacher_name`, `class_name`, `total`, `is_stop`, `send_email`) VALUES (1009, 5, 'kuman', 5, 8083, 6, '2023-04-26 01:50:13.000000', '2023-04-26 03:50:13.000000', 'afa98dd0-e3d4-11ed-a002-6d956c1f21f5', '25', '董自贡老师', '课室3班', '70', 1, 0);
INSERT INTO `login_estimatehistory` (`id`, `sid`, `who`, `who_id`, `port`, `type_detail`, `setting_time`, `expired_time`, `class_info_id`, `class_room_name`, `teacher_name`, `class_name`, `total`, `is_stop`, `send_email`) VALUES (1010, 1, 'kuman', 5, 8082, 11, '2023-04-26 02:54:23.000000', '2023-04-26 04:54:23.000000', 'a6559ea0-e3dd-11ed-9444-b3810c1c4e18', '25', '测试的', '测试的班级', '100', 0, 0);
COMMIT;

-- ----------------------------
-- Table structure for login_frontendshow
-- ----------------------------
DROP TABLE IF EXISTS `login_frontendshow`;
CREATE TABLE `login_frontendshow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` char(39) NOT NULL,
  `port` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `switch_addr` varchar(255) DEFAULT NULL,
  `acl_uuid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `login_frontendshow_location_id_51b54db6_fk_login_location_id` (`location_id`) USING BTREE,
  CONSTRAINT `login_frontendshow_location_id_51b54db6_fk_login_location_id` FOREIGN KEY (`location_id`) REFERENCES `login_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_frontendshow
-- ----------------------------
BEGIN;
INSERT INTO `login_frontendshow` (`id`, `ip`, `port`, `location_id`, `switch_addr`, `acl_uuid`) VALUES (2, '192.168.10.35', 80, 1, '192.168.10.21', 'ae781adde98440deb7188e9d7c257a49');
COMMIT;

-- ----------------------------
-- Table structure for login_iewaycookie
-- ----------------------------
DROP TABLE IF EXISTS `login_iewaycookie`;
CREATE TABLE `login_iewaycookie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cookie_value` varchar(200) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_iewaycookie
-- ----------------------------
BEGIN;
INSERT INTO `login_iewaycookie` (`id`, `cookie_value`) VALUES (1, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNjE5MF9wYyIsImV4cCI6MTY4MDk2MzYxMSwiaWF0IjoxNjgwOTIwNDExfQ.tf_XQZHanPM2vnadBLfljsj2O-WUGi6I07_RbaGhqqM');
COMMIT;

-- ----------------------------
-- Table structure for login_location
-- ----------------------------
DROP TABLE IF EXISTS `login_location`;
CREATE TABLE `login_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) NOT NULL,
  `location_name` varchar(60) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_location
-- ----------------------------
BEGIN;
INSERT INTO `login_location` (`id`, `tid`, `location_name`, `description`) VALUES (1, 0, '798艺术园B幢', '798艺术园B幢');
INSERT INTO `login_location` (`id`, `tid`, `location_name`, `description`) VALUES (2, 1, '2楼', '2楼');
COMMIT;

-- ----------------------------
-- Table structure for login_porttype
-- ----------------------------
DROP TABLE IF EXISTS `login_porttype`;
CREATE TABLE `login_porttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `port` int(11) DEFAULT NULL,
  `rname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_porttype
-- ----------------------------
BEGIN;
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (1, 0, '讲师', 8081, 'jiangshi');
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (2, 0, '班主任', 8091, 'banzhuren');
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (3, 0, '辅导员', 8071, 'fudaoyuan');
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (6, 1, '不可设置-', NULL, NULL);
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (7, 2, '班主任', NULL, NULL);
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (8, 3, '辅导员', NULL, NULL);
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (11, 1, '基础班-讲师', NULL, 'java-jichu');
INSERT INTO `login_porttype` (`id`, `tid`, `type`, `port`, `rname`) VALUES (12, 1, '大神班-讲师', NULL, 'java-dashen');
COMMIT;

-- ----------------------------
-- Table structure for login_subjectdetail
-- ----------------------------
DROP TABLE IF EXISTS `login_subjectdetail`;
CREATE TABLE `login_subjectdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) NOT NULL,
  `subject_name` varchar(50) NOT NULL,
  `subject_teacher_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_subjectdetail
-- ----------------------------
BEGIN;
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (1, 0, 'iOS', NULL, 'iOS学院');
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (2, 0, 'android', NULL, '安卓学院');
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (3, 0, 'java', NULL, 'java学院');
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (4, 0, 'C++', NULL, 'C++学院');
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (5, 0, 'UI', NULL, 'UI学院');
INSERT INTO `login_subjectdetail` (`id`, `tid`, `subject_name`, `subject_teacher_name`, `description`) VALUES (6, 0, 'HTML5', NULL, 'H5学院');
COMMIT;

-- ----------------------------
-- Table structure for register_verifyinfo
-- ----------------------------
DROP TABLE IF EXISTS `register_verifyinfo`;
CREATE TABLE `register_verifyinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `register_code` varchar(10) NOT NULL,
  `expired_time` datetime(6) NOT NULL,
  `times` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of register_verifyinfo
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

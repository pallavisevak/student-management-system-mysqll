import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sms2"
)
mycursor = mydb.cursor()
# mycursor.execute("create table attendance(attendance_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT,FOREIGN KEY (student_id) REFERENCES students(student_id),class_id INT,FOREIGN KEY (class_id) REFERENCES classes(class_id),attendance_date VARCHAR(20),present VARCHAR(10))")
sql = "INSERT INTO attendance(student_id,class_id,attendance_date,present) VALUES (%s,%s,%s,%s)"
val=[
(1,1,'2023/12/01','True'),
(2,1,'2023/12/01','False'),
(3,1,'2023/12/01','False'),
(4,1,'2023/12/01','False'),
(5,1,'2023/12/01','False'),
(6,1,'2023/12/01','True'),
(7,1,'2023/12/01','True'),
(8,1,'2023/12/01','True'),
(9,1,'2023/12/01','True'),
(10,1,'2023/12/01','False'),
(11,1,'2023/12/01','False'),
(12,1,'2023/12/01','False'),
(13,1,'2023/12/01','True'),
(14,1,'2023/12/01','True'),
(15,1,'2023/12/01','False'),
(16,1,'2023/12/01','True'),
(17,1,'2023/12/01','True'),
(18,1,'2023/12/01','False'),
(19,1,'2023/12/01','True'),
(20,1,'2023/12/01','False'),
(21,1,'2023/12/01','False'),
(22,1,'2023/12/01','False'),
(23,1,'2023/12/01','False'),
(24,1,'2023/12/01','True'),
(25,1,'2023/12/01','False'),
(26,1,'2023/12/01','True'),
(27,1,'2023/12/01','True'),
(28,1,'2023/12/01','True'),
(29,1,'2023/12/01','True'),
(30,1,'2023/12/01','False'),
(31,1,'2023/12/01','True'),
(32,1,'2023/12/01','False'),
(33,1,'2023/12/01','False'),
(34,1,'2023/12/01','False'),
(35,1,'2023/12/01','True'),
(36,1,'2023/12/01','False'),
(37,1,'2023/12/01','False'),
(38,1,'2023/12/01','True'),
(39,1,'2023/12/01','True'),
(40,1,'2023/12/01','False'),
(41,1,'2023/12/01','False'),
(42,1,'2023/12/01','True'),
(43,1,'2023/12/01','False'),
(44,1,'2023/12/01','False'),
(45,1,'2023/12/01','False'),
(46,1,'2023/12/01','True'),
(47,1,'2023/12/01','False'),
(48,1,'2023/12/01','False'),
(49,1,'2023/12/01','False'),
(50,1,'2023/12/01','False'),
(51,1,'2023/12/01','False'),
(52,1,'2023/12/01','True'),
(53,1,'2023/12/01','True'),
(54,1,'2023/12/01','False'),
(55,1,'2023/12/01','True'),
(56,1,'2023/12/01','False'),
(57,1,'2023/12/01','False'),
(58,1,'2023/12/01','True'),
(59,1,'2023/12/01','False'),
(60,1,'2023/12/01','True'),
(61,1,'2023/12/01','False'),
(62,1,'2023/12/01','True'),
(63,2,'2023/12/01','False'),
(64,2,'2023/12/01','False'),
(65,2,'2023/12/01','True'),
(66,2,'2023/12/01','True'),
(67,2,'2023/12/01','False'),
(68,2,'2023/12/01','True'),
(69,2,'2023/12/01','False'),
(70,2,'2023/12/01','True'),
(71,2,'2023/12/01','False'),
(72,2,'2023/12/01','True'),
(73,2,'2023/12/01','False'),
(74,2,'2023/12/01','True'),
(75,2,'2023/12/01','False'),
(76,2,'2023/12/01','True'),
(77,2,'2023/12/01','True'),
(78,2,'2023/12/01','False'),
(79,2,'2023/12/01','False'),
(80,2,'2023/12/01','False'),
(81,2,'2023/12/01','True'),
(82,2,'2023/12/01','True'),
(83,2,'2023/12/01','False'),
(84,2,'2023/12/01','True'),
(85,2,'2023/12/01','False'),
(86,2,'2023/12/01','True'),
(87,2,'2023/12/01','False'),
(88,2,'2023/12/01','True'),
(89,2,'2023/12/01','True'),
(90,2,'2023/12/01','False'),
(91,2,'2023/12/01','True'),
(92,2,'2023/12/01','True'),
(93,2,'2023/12/01','True'),
(94,2,'2023/12/01','True'),
(95,2,'2023/12/01','False'),
(96,2,'2023/12/01','True'),
(97,2,'2023/12/01','False'),
(98,2,'2023/12/01','True'),
(99,2,'2023/12/01','False'),
(100,2,'2023/12/01','False'),
(101,2,'2023/12/01','False'),
(102,2,'2023/12/01','True'),
(103,2,'2023/12/01','True'),
(104,2,'2023/12/01','True'),
(105,2,'2023/12/01','True'),
(106,2,'2023/12/01','True'),
(107,2,'2023/12/01','True'),
(108,2,'2023/12/01','True'),
(109,2,'2023/12/01','True'),
(110,2,'2023/12/01','True'),
(111,2,'2023/12/01','False'),
(112,2,'2023/12/01','True'),
(113,2,'2023/12/01','False'),
(114,2,'2023/12/01','True'),
(115,2,'2023/12/01','True'),
(116,2,'2023/12/01','False'),
(117,2,'2023/12/01','False'),
(118,2,'2023/12/01','True'),
(119,2,'2023/12/01','True'),
(120,2,'2023/12/01','True'),
(121,2,'2023/12/01','True'),
(122,2,'2023/12/01','False'),
(123,2,'2023/12/01','False'),
(124,2,'2023/12/01','False'),
(125,3,'2023/12/01','False'),
(126,3,'2023/12/01','True'),
(127,3,'2023/12/01','True'),
(128,3,'2023/12/01','True'),
(129,3,'2023/12/01','True'),
(130,3,'2023/12/01','False'),
(131,3,'2023/12/01','False'),
(132,3,'2023/12/01','False'),
(133,3,'2023/12/01','True'),
(134,3,'2023/12/01','False'),
(135,3,'2023/12/01','True'),
(136,3,'2023/12/01','False'),
(137,3,'2023/12/01','True'),
(138,3,'2023/12/01','False'),
(139,3,'2023/12/01','False'),
(140,3,'2023/12/01','True'),
(141,3,'2023/12/01','True'),
(142,3,'2023/12/01','False'),
(143,3,'2023/12/01','True'),
(144,3,'2023/12/01','True'),
(145,3,'2023/12/01','False'),
(146,3,'2023/12/01','False'),
(147,3,'2023/12/01','True'),
(148,3,'2023/12/01','False'),
(149,3,'2023/12/01','False'),
(150,3,'2023/12/01','False'),
(151,3,'2023/12/01','True'),
(152,3,'2023/12/01','False'),
(153,3,'2023/12/01','True'),
(154,3,'2023/12/01','True'),
(155,3,'2023/12/01','True'),
(156,3,'2023/12/01','False'),
(157,3,'2023/12/01','True'),
(158,3,'2023/12/01','False'),
(159,3,'2023/12/01','True'),
(160,3,'2023/12/01','False'),
(161,3,'2023/12/01','True'),
(162,3,'2023/12/01','True'),
(163,3,'2023/12/01','False'),
(164,3,'2023/12/01','False'),
(165,3,'2023/12/01','True'),
(166,3,'2023/12/01','False'),
(167,3,'2023/12/01','True'),
(168,3,'2023/12/01','True'),
(169,3,'2023/12/01','False'),
(170,3,'2023/12/01','False'),
(171,3,'2023/12/01','True'),
(172,3,'2023/12/01','True'),
(173,3,'2023/12/01','False'),
(174,3,'2023/12/01','False'),
(175,3,'2023/12/01','False'),
(176,3,'2023/12/01','True'),
(177,3,'2023/12/01','False'),
(178,3,'2023/12/01','False'),
(179,3,'2023/12/01','False'),
(180,3,'2023/12/01','True'),
(181,3,'2023/12/01','True'),
(182,3,'2023/12/01','True'),
(183,3,'2023/12/01','False'),
(184,3,'2023/12/01','False'),
(185,3,'2023/12/01','False'),
(186,3,'2023/12/01','True'),
(187,4,'2023/12/01','True'),
(188,4,'2023/12/01','True'),
(189,4,'2023/12/01','False'),
(190,4,'2023/12/01','True'),
(191,4,'2023/12/01','True'),
(192,4,'2023/12/01','False'),
(193,4,'2023/12/01','True'),
(194,4,'2023/12/01','True'),
(195,4,'2023/12/01','True'),
(196,4,'2023/12/01','True'),
(197,4,'2023/12/01','True'),
(198,4,'2023/12/01','False'),
(199,4,'2023/12/01','False'),
(200,4,'2023/12/01','True'),
(201,4,'2023/12/01','True'),
(202,4,'2023/12/01','True'),
(203,4,'2023/12/01','True'),
(204,4,'2023/12/01','False'),
(205,4,'2023/12/01','True'),
(206,4,'2023/12/01','False'),
(207,4,'2023/12/01','True'),
(208,4,'2023/12/01','False'),
(209,4,'2023/12/01','False'),
(210,4,'2023/12/01','True'),
(211,4,'2023/12/01','True'),
(212,4,'2023/12/01','True'),
(213,4,'2023/12/01','False'),
(214,4,'2023/12/01','True'),
(215,4,'2023/12/01','True'),
(216,4,'2023/12/01','False'),
(217,4,'2023/12/01','False'),
(218,4,'2023/12/01','True'),
(219,4,'2023/12/01','True'),
(220,4,'2023/12/01','False'),
(221,4,'2023/12/01','False'),
(222,4,'2023/12/01','True'),
(223,4,'2023/12/01','False'),
(224,4,'2023/12/01','True'),
(225,4,'2023/12/01','False'),
(226,4,'2023/12/01','False'),
(227,4,'2023/12/01','True'),
(228,4,'2023/12/01','False'),
(229,4,'2023/12/01','False'),
(230,4,'2023/12/01','False'),
(231,4,'2023/12/01','True'),
(232,4,'2023/12/01','False'),
(233,4,'2023/12/01','False'),
(234,4,'2023/12/01','False'),
(235,4,'2023/12/01','False'),
(236,4,'2023/12/01','True'),
(237,4,'2023/12/01','True'),
(238,4,'2023/12/01','True'),
(239,4,'2023/12/01','True'),
(240,4,'2023/12/01','True'),
(241,4,'2023/12/01','False'),
(242,4,'2023/12/01','True'),
(243,4,'2023/12/01','False'),
(244,4,'2023/12/01','False'),
(245,4,'2023/12/01','False'),
(246,4,'2023/12/01','True'),
(247,4,'2023/12/01','True'),
(248,4,'2023/12/01','False'),
(249,5,'2023/12/01','True'),
(250,5,'2023/12/01','True'),
(251,5,'2023/12/01','False'),
(252,5,'2023/12/01','True'),
(253,5,'2023/12/01','False'),
(254,5,'2023/12/01','False'),
(255,5,'2023/12/01','True'),
(256,5,'2023/12/01','True'),
(257,5,'2023/12/01','True'),
(258,5,'2023/12/01','False'),
(259,5,'2023/12/01','True'),
(260,5,'2023/12/01','True'),
(261,5,'2023/12/01','False'),
(262,5,'2023/12/01','True'),
(263,5,'2023/12/01','False'),
(264,5,'2023/12/01','False'),
(265,5,'2023/12/01','True'),
(266,5,'2023/12/01','True'),
(267,5,'2023/12/01','True'),
(268,5,'2023/12/01','False'),
(269,5,'2023/12/01','False'),
(270,5,'2023/12/01','True'),
(271,5,'2023/12/01','True'),
(272,5,'2023/12/01','True'),
(273,5,'2023/12/01','True'),
(274,5,'2023/12/01','False'),
(275,5,'2023/12/01','True'),
(276,5,'2023/12/01','False'),
(277,5,'2023/12/01','True'),
(278,5,'2023/12/01','True'),
(279,5,'2023/12/01','True'),
(280,5,'2023/12/01','False'),
(281,5,'2023/12/01','True'),
(282,5,'2023/12/01','False'),
(283,5,'2023/12/01','False'),
(284,5,'2023/12/01','True'),
(285,5,'2023/12/01','False'),
(286,5,'2023/12/01','True'),
(287,5,'2023/12/01','True'),
(288,5,'2023/12/01','False'),
(289,5,'2023/12/01','True'),
(290,5,'2023/12/01','False'),
(291,5,'2023/12/01','True'),
(292,5,'2023/12/01','False'),
(293,5,'2023/12/01','False'),
(294,5,'2023/12/01','False'),
(295,5,'2023/12/01','True'),
(296,5,'2023/12/01','True'),
(297,5,'2023/12/01','True'),
(298,5,'2023/12/01','True'),
(299,5,'2023/12/01','False'),
(300,5,'2023/12/01','False'),
(301,5,'2023/12/01','False'),
(302,5,'2023/12/01','True'),
(303,5,'2023/12/01','False'),
(304,5,'2023/12/01','True'),
(305,5,'2023/12/01','True'),
(306,5,'2023/12/01','False'),
(307,5,'2023/12/01','True'),
(308,5,'2023/12/01','False'),
(309,5,'2023/12/01','False'),
(310,5,'2023/12/01','True'),
(311,6,'2023/12/01','False'),
(312,6,'2023/12/01','False'),
(313,6,'2023/12/01','False'),
(314,6,'2023/12/01','True'),
(315,6,'2023/12/01','True'),
(316,6,'2023/12/01','False'),
(317,6,'2023/12/01','True'),
(318,6,'2023/12/01','True'),
(319,6,'2023/12/01','True'),
(320,6,'2023/12/01','True'),
(321,6,'2023/12/01','False'),
(322,6,'2023/12/01','False'),
(323,6,'2023/12/01','False'),
(324,6,'2023/12/01','True'),
(325,6,'2023/12/01','True'),
(326,6,'2023/12/01','True'),
(327,6,'2023/12/01','False'),
(328,6,'2023/12/01','True'),
(329,6,'2023/12/01','False'),
(330,6,'2023/12/01','True'),
(331,6,'2023/12/01','True'),
(332,6,'2023/12/01','False'),
(333,6,'2023/12/01','False'),
(334,6,'2023/12/01','False'),
(335,6,'2023/12/01','False'),
(336,6,'2023/12/01','False'),
(337,6,'2023/12/01','True'),
(338,6,'2023/12/01','True'),
(339,6,'2023/12/01','False'),
(340,6,'2023/12/01','True'),
(341,6,'2023/12/01','False'),
(342,6,'2023/12/01','False'),
(343,6,'2023/12/01','True'),
(344,6,'2023/12/01','True'),
(345,6,'2023/12/01','True'),
(346,6,'2023/12/01','False'),
(347,6,'2023/12/01','True'),
(348,6,'2023/12/01','True'),
(349,6,'2023/12/01','True'),
(350,6,'2023/12/01','True'),
(351,6,'2023/12/01','True'),
(352,6,'2023/12/01','True'),
(353,6,'2023/12/01','False'),
(354,6,'2023/12/01','True'),
(355,6,'2023/12/01','False'),
(356,6,'2023/12/01','False'),
(357,6,'2023/12/01','False'),
(358,6,'2023/12/01','True'),
(359,6,'2023/12/01','False'),
(360,6,'2023/12/01','True'),
(361,6,'2023/12/01','False'),
(362,6,'2023/12/01','True'),
(363,6,'2023/12/01','True'),
(364,6,'2023/12/01','True'),
(365,6,'2023/12/01','False'),
(366,6,'2023/12/01','True'),
(367,6,'2023/12/01','True'),
(368,6,'2023/12/01','True'),
(369,6,'2023/12/01','True'),
(370,6,'2023/12/01','True'),
(371,6,'2023/12/01','True'),
(372,6,'2023/12/01','True'),
(373,7,'2023/12/01','True'),
(374,7,'2023/12/01','False'),
(375,7,'2023/12/01','True'),
(376,7,'2023/12/01','False'),
(377,7,'2023/12/01','True'),
(378,7,'2023/12/01','False'),
(379,7,'2023/12/01','True'),
(380,7,'2023/12/01','False'),
(381,7,'2023/12/01','False'),
(382,7,'2023/12/01','True'),
(383,7,'2023/12/01','False'),
(384,7,'2023/12/01','False'),
(385,7,'2023/12/01','True'),
(386,7,'2023/12/01','True'),
(387,7,'2023/12/01','False'),
(388,7,'2023/12/01','False'),
(389,7,'2023/12/01','True'),
(390,7,'2023/12/01','False'),
(391,7,'2023/12/01','False'),
(392,7,'2023/12/01','True'),
(393,7,'2023/12/01','True'),
(394,7,'2023/12/01','True'),
(395,7,'2023/12/01','True'),
(396,7,'2023/12/01','True'),
(397,7,'2023/12/01','False'),
(398,7,'2023/12/01','True'),
(399,7,'2023/12/01','True'),
(400,7,'2023/12/01','True'),
(401,7,'2023/12/01','True'),
(402,7,'2023/12/01','False'),
(403,7,'2023/12/01','False'),
(404,7,'2023/12/01','True'),
(405,7,'2023/12/01','False'),
(406,7,'2023/12/01','True'),
(407,7,'2023/12/01','True'),
(408,7,'2023/12/01','False'),
(409,7,'2023/12/01','True'),
(410,7,'2023/12/01','False'),
(411,7,'2023/12/01','False'),
(412,7,'2023/12/01','True'),
(413,7,'2023/12/01','False'),
(414,7,'2023/12/01','False'),
(415,7,'2023/12/01','True'),
(416,7,'2023/12/01','False'),
(417,7,'2023/12/01','True'),
(418,7,'2023/12/01','True'),
(419,7,'2023/12/01','False'),
(420,7,'2023/12/01','True'),
(421,7,'2023/12/01','True'),
(422,7,'2023/12/01','False'),
(423,7,'2023/12/01','True'),
(424,7,'2023/12/01','True'),
(425,7,'2023/12/01','True'),
(426,7,'2023/12/01','False'),
(427,7,'2023/12/01','True'),
(428,7,'2023/12/01','True'),
(429,7,'2023/12/01','False'),
(430,7,'2023/12/01','False'),
(431,7,'2023/12/01','True'),
(432,7,'2023/12/01','True'),
(433,7,'2023/12/01','False'),
(434,7,'2023/12/01','True'),
(435,8,'2023/12/01','False'),
(436,8,'2023/12/01','True'),
(437,8,'2023/12/01','True'),
(438,8,'2023/12/01','True'),
(439,8,'2023/12/01','True'),
(440,8,'2023/12/01','True'),
(441,8,'2023/12/01','False'),
(442,8,'2023/12/01','False'),
(443,8,'2023/12/01','True'),
(444,8,'2023/12/01','False'),
(445,8,'2023/12/01','False'),
(446,8,'2023/12/01','False'),
(447,8,'2023/12/01','False'),
(448,8,'2023/12/01','True'),
(449,8,'2023/12/01','True'),
(450,8,'2023/12/01','True'),
(451,8,'2023/12/01','True'),
(452,8,'2023/12/01','True'),
(453,8,'2023/12/01','False'),
(454,8,'2023/12/01','False'),
(455,8,'2023/12/01','False'),
(456,8,'2023/12/01','True'),
(457,8,'2023/12/01','False'),
(458,8,'2023/12/01','True'),
(459,8,'2023/12/01','False'),
(460,8,'2023/12/01','True'),
(461,8,'2023/12/01','False'),
(462,8,'2023/12/01','True'),
(463,8,'2023/12/01','True'),
(464,8,'2023/12/01','False'),
(465,8,'2023/12/01','False'),
(466,8,'2023/12/01','False'),
(467,8,'2023/12/01','False'),
(468,8,'2023/12/01','False'),
(469,8,'2023/12/01','False'),
(470,8,'2023/12/01','False'),
(471,8,'2023/12/01','True'),
(472,8,'2023/12/01','True'),
(473,8,'2023/12/01','False'),
(474,8,'2023/12/01','True'),
(475,8,'2023/12/01','True'),
(476,8,'2023/12/01','True'),
(477,8,'2023/12/01','True'),
(478,8,'2023/12/01','False'),
(479,8,'2023/12/01','True'),
(480,8,'2023/12/01','True'),
(481,8,'2023/12/01','False'),
(482,8,'2023/12/01','False'),
(483,8,'2023/12/01','True'),
(484,8,'2023/12/01','False'),
(485,8,'2023/12/01','False'),
(486,8,'2023/12/01','True'),
(487,8,'2023/12/01','False'),
(488,8,'2023/12/01','True'),
(489,8,'2023/12/01','True'),
(490,8,'2023/12/01','False'),
(491,8,'2023/12/01','False'),
(492,8,'2023/12/01','True'),
(493,8,'2023/12/01','False'),
(494,8,'2023/12/01','True'),
(495,8,'2023/12/01','False'),
(496,8,'2023/12/01','True'),
(497,9,'2023/12/01','True'),
(498,9,'2023/12/01','True'),
(499,9,'2023/12/01','False'),
(500,9,'2023/12/01','False'),
(501,9,'2023/12/01','False'),
(502,9,'2023/12/01','True'),
(503,9,'2023/12/01','True'),
(504,9,'2023/12/01','True'),
(505,9,'2023/12/01','False'),
(506,9,'2023/12/01','False'),
(507,9,'2023/12/01','True'),
(508,9,'2023/12/01','False'),
(509,9,'2023/12/01','True'),
(510,9,'2023/12/01','True'),
(511,9,'2023/12/01','False'),
(512,9,'2023/12/01','True'),
(513,9,'2023/12/01','False'),
(514,9,'2023/12/01','False'),
(515,9,'2023/12/01','False'),
(516,9,'2023/12/01','True'),
(517,9,'2023/12/01','True'),
(518,9,'2023/12/01','True'),
(519,9,'2023/12/01','False'),
(520,9,'2023/12/01','False'),
(521,9,'2023/12/01','False'),
(522,9,'2023/12/01','False'),
(523,9,'2023/12/01','False'),
(524,9,'2023/12/01','False'),
(525,9,'2023/12/01','True'),
(526,9,'2023/12/01','True'),
(527,9,'2023/12/01','False'),
(528,9,'2023/12/01','False'),
(529,9,'2023/12/01','True'),
(530,9,'2023/12/01','True'),
(531,9,'2023/12/01','False'),
(532,9,'2023/12/01','True'),
(533,9,'2023/12/01','True'),
(534,9,'2023/12/01','True'),
(535,9,'2023/12/01','True'),
(536,9,'2023/12/01','False'),
(537,9,'2023/12/01','True'),
(538,9,'2023/12/01','True'),
(539,9,'2023/12/01','False'),
(540,9,'2023/12/01','True'),
(541,9,'2023/12/01','True'),
(542,9,'2023/12/01','True'),
(543,9,'2023/12/01','True'),
(544,9,'2023/12/01','False'),
(545,9,'2023/12/01','False'),
(546,9,'2023/12/01','False'),
(547,9,'2023/12/01','True'),
(548,9,'2023/12/01','True'),
(549,9,'2023/12/01','False'),
(550,9,'2023/12/01','False'),
(551,9,'2023/12/01','True'),
(552,9,'2023/12/01','False'),
(553,9,'2023/12/01','False'),
(554,9,'2023/12/01','True'),
(555,9,'2023/12/01','True'),
(556,9,'2023/12/01','True'),
(557,9,'2023/12/01','True'),
(558,9,'2023/12/01','True'),
(559,10,'2023/12/01','True'),
(560,10,'2023/12/01','False'),
(561,10,'2023/12/01','False'),
(562,10,'2023/12/01','True'),
(563,10,'2023/12/01','False'),
(564,10,'2023/12/01','True'),
(565,10,'2023/12/01','False'),
(566,10,'2023/12/01','False'),
(567,10,'2023/12/01','False'),
(568,10,'2023/12/01','False'),
(569,10,'2023/12/01','True'),
(570,10,'2023/12/01','False'),
(571,10,'2023/12/01','False'),
(572,10,'2023/12/01','True'),
(573,10,'2023/12/01','True'),
(574,10,'2023/12/01','False'),
(575,10,'2023/12/01','False'),
(576,10,'2023/12/01','False'),
(577,10,'2023/12/01','False'),
(578,10,'2023/12/01','False'),
(579,10,'2023/12/01','False'),
(580,10,'2023/12/01','False'),
(581,10,'2023/12/01','False'),
(582,10,'2023/12/01','False'),
(583,10,'2023/12/01','False'),
(584,10,'2023/12/01','True'),
(585,10,'2023/12/01','False'),
(586,10,'2023/12/01','False'),
(587,10,'2023/12/01','False'),
(588,10,'2023/12/01','False'),
(589,10,'2023/12/01','False'),
(590,10,'2023/12/01','False'),
(591,10,'2023/12/01','False'),
(592,10,'2023/12/01','True'),
(593,10,'2023/12/01','True'),
(594,10,'2023/12/01','True'),
(595,10,'2023/12/01','False'),
(596,10,'2023/12/01','False'),
(597,10,'2023/12/01','False'),
(598,10,'2023/12/01','False'),
(599,10,'2023/12/01','False'),
(600,10,'2023/12/01','False'),
(601,10,'2023/12/01','True'),
(602,10,'2023/12/01','True'),
(603,10,'2023/12/01','True'),
(604,10,'2023/12/01','True'),
(605,10,'2023/12/01','True'),
(606,10,'2023/12/01','True'),
(607,10,'2023/12/01','False'),
(608,10,'2023/12/01','False'),
(609,10,'2023/12/01','False'),
(610,10,'2023/12/01','True'),
(611,10,'2023/12/01','False'),
(612,10,'2023/12/01','True'),
(613,10,'2023/12/01','False'),
(614,10,'2023/12/01','False'),
(615,10,'2023/12/01','True'),
(616,10,'2023/12/01','True'),
(617,10,'2023/12/01','False'),
(618,10,'2023/12/01','False'),
(619,10,'2023/12/01','True'),
(620,10,'2023/12/01','True'),
(621,11,'2023/12/01','False'),
(622,11,'2023/12/01','False'),
(623,11,'2023/12/01','False'),
(624,11,'2023/12/01','True'),
(625,11,'2023/12/01','True'),
(626,11,'2023/12/01','False'),
(627,11,'2023/12/01','True'),
(628,11,'2023/12/01','False'),
(629,11,'2023/12/01','True'),
(630,11,'2023/12/01','False'),
(631,11,'2023/12/01','True'),
(632,11,'2023/12/01','True'),
(633,11,'2023/12/01','False'),
(634,11,'2023/12/01','True'),
(635,11,'2023/12/01','True'),
(636,11,'2023/12/01','False'),
(637,11,'2023/12/01','True'),
(638,11,'2023/12/01','False'),
(639,11,'2023/12/01','False'),
(640,11,'2023/12/01','False'),
(641,11,'2023/12/01','False'),
(642,11,'2023/12/01','False'),
(643,11,'2023/12/01','True'),
(644,11,'2023/12/01','False'),
(645,11,'2023/12/01','False'),
(646,11,'2023/12/01','True'),
(647,11,'2023/12/01','True'),
(648,11,'2023/12/01','False'),
(649,11,'2023/12/01','False'),
(650,11,'2023/12/01','True'),
(651,11,'2023/12/01','True'),
(652,11,'2023/12/01','True'),
(653,11,'2023/12/01','True'),
(654,11,'2023/12/01','True'),
(655,11,'2023/12/01','True'),
(656,11,'2023/12/01','False'),
(657,11,'2023/12/01','False'),
(658,11,'2023/12/01','False'),
(659,11,'2023/12/01','False'),
(660,11,'2023/12/01','True'),
(661,11,'2023/12/01','True'),
(662,11,'2023/12/01','True'),
(663,11,'2023/12/01','False'),
(664,11,'2023/12/01','True'),
(665,11,'2023/12/01','True'),
(666,11,'2023/12/01','True'),
(667,11,'2023/12/01','True'),
(668,11,'2023/12/01','False'),
(669,11,'2023/12/01','True'),
(670,11,'2023/12/01','False'),
(671,11,'2023/12/01','True'),
(672,11,'2023/12/01','True'),
(673,11,'2023/12/01','True'),
(674,11,'2023/12/01','True'),
(675,11,'2023/12/01','False'),
(676,11,'2023/12/01','False'),
(677,11,'2023/12/01','True'),
(678,11,'2023/12/01','False'),
(679,11,'2023/12/01','True'),
(680,11,'2023/12/01','False'),
(681,11,'2023/12/01','False'),
(682,11,'2023/12/01','False'),
(683,12,'2023/12/01','True'),
(684,12,'2023/12/01','False'),
(685,12,'2023/12/01','True'),
(686,12,'2023/12/01','True'),
(687,12,'2023/12/01','False'),
(688,12,'2023/12/01','False'),
(689,12,'2023/12/01','False'),
(690,12,'2023/12/01','True'),
(691,12,'2023/12/01','False'),
(692,12,'2023/12/01','True'),
(693,12,'2023/12/01','False'),
(694,12,'2023/12/01','False'),
(695,12,'2023/12/01','False'),
(696,12,'2023/12/01','True'),
(697,12,'2023/12/01','False'),
(698,12,'2023/12/01','False'),
(699,12,'2023/12/01','True'),
(700,12,'2023/12/01','True'),
(701,12,'2023/12/01','True'),
(702,12,'2023/12/01','True'),
(703,12,'2023/12/01','True'),
(704,12,'2023/12/01','False'),
(705,12,'2023/12/01','True'),
(706,12,'2023/12/01','False'),
(707,12,'2023/12/01','False'),
(708,12,'2023/12/01','True'),
(709,12,'2023/12/01','True'),
(710,12,'2023/12/01','False'),
(711,12,'2023/12/01','False'),
(712,12,'2023/12/01','True'),
(713,12,'2023/12/01','True'),
(714,12,'2023/12/01','False'),
(715,12,'2023/12/01','False'),
(716,12,'2023/12/01','False'),
(717,12,'2023/12/01','True'),
(718,12,'2023/12/01','False'),
(719,12,'2023/12/01','False'),
(720,12,'2023/12/01','False'),
(721,12,'2023/12/01','True'),
(722,12,'2023/12/01','True'),
(723,12,'2023/12/01','True'),
(724,12,'2023/12/01','False'),
(725,12,'2023/12/01','True'),
(726,12,'2023/12/01','True'),
(727,12,'2023/12/01','False'),
(728,12,'2023/12/01','True'),
(729,12,'2023/12/01','True'),
(730,12,'2023/12/01','False'),
(731,12,'2023/12/01','True'),
(732,12,'2023/12/01','False'),
(733,12,'2023/12/01','False'),
(734,12,'2023/12/01','True'),
(735,12,'2023/12/01','True'),
(736,12,'2023/12/01','True'),
(737,12,'2023/12/01','False'),
(738,12,'2023/12/01','True'),
(739,12,'2023/12/01','True'),
(740,12,'2023/12/01','True'),
(741,12,'2023/12/01','True'),
(742,12,'2023/12/01','True'),
(743,12,'2023/12/01','True'),
(744,12,'2023/12/01','False'),
(745,13,'2023/12/01','False'),
(746,13,'2023/12/01','False'),
(747,13,'2023/12/01','True'),
(748,13,'2023/12/01','False'),
(749,13,'2023/12/01','True'),
(750,13,'2023/12/01','True'),
(751,13,'2023/12/01','False'),
(752,13,'2023/12/01','False'),
(753,13,'2023/12/01','False'),
(754,13,'2023/12/01','True'),
(755,13,'2023/12/01','True'),
(756,13,'2023/12/01','False'),
(757,13,'2023/12/01','True'),
(758,13,'2023/12/01','False'),
(759,13,'2023/12/01','True'),
(760,13,'2023/12/01','True'),
(761,13,'2023/12/01','True'),
(762,13,'2023/12/01','False'),
(763,13,'2023/12/01','True'),
(764,13,'2023/12/01','True'),
(765,13,'2023/12/01','False'),
(766,13,'2023/12/01','True'),
(767,13,'2023/12/01','False'),
(768,13,'2023/12/01','True'),
(769,13,'2023/12/01','True'),
(770,13,'2023/12/01','True'),
(771,13,'2023/12/01','False'),
(772,13,'2023/12/01','True'),
(773,13,'2023/12/01','False'),
(774,13,'2023/12/01','False'),
(775,13,'2023/12/01','True'),
(776,13,'2023/12/01','True'),
(777,13,'2023/12/01','False'),
(778,13,'2023/12/01','True'),
(779,13,'2023/12/01','True'),
(780,13,'2023/12/01','False'),
(781,13,'2023/12/01','True'),
(782,13,'2023/12/01','True'),
(783,13,'2023/12/01','False'),
(784,13,'2023/12/01','True'),
(785,13,'2023/12/01','True'),
(786,13,'2023/12/01','False'),
(787,13,'2023/12/01','False'),
(788,13,'2023/12/01','False'),
(789,13,'2023/12/01','False'),
(790,13,'2023/12/01','False'),
(791,13,'2023/12/01','False'),
(792,13,'2023/12/01','True'),
(793,13,'2023/12/01','True'),
(794,13,'2023/12/01','False'),
(795,13,'2023/12/01','True'),
(796,13,'2023/12/01','True'),
(797,13,'2023/12/01','True'),
(798,13,'2023/12/01','False'),
(799,13,'2023/12/01','False'),
(800,13,'2023/12/01','True'),
(801,13,'2023/12/01','False'),
(802,13,'2023/12/01','False'),
(803,13,'2023/12/01','False'),
(804,13,'2023/12/01','False'),
(805,13,'2023/12/01','True'),
(806,13,'2023/12/01','True'),
(807,14,'2023/12/01','True'),
(808,14,'2023/12/01','True'),
(809,14,'2023/12/01','False'),
(810,14,'2023/12/01','True'),
(811,14,'2023/12/01','True'),
(812,14,'2023/12/01','True'),
(813,14,'2023/12/01','True'),
(814,14,'2023/12/01','False'),
(815,14,'2023/12/01','True'),
(816,14,'2023/12/01','True'),
(817,14,'2023/12/01','True'),
(818,14,'2023/12/01','False'),
(819,14,'2023/12/01','False'),
(820,14,'2023/12/01','True'),
(821,14,'2023/12/01','True'),
(822,14,'2023/12/01','True'),
(823,14,'2023/12/01','True'),
(824,14,'2023/12/01','False'),
(825,14,'2023/12/01','False'),
(826,14,'2023/12/01','False'),
(827,14,'2023/12/01','False'),
(828,14,'2023/12/01','True'),
(829,14,'2023/12/01','True'),
(830,14,'2023/12/01','True'),
(831,14,'2023/12/01','True'),
(832,14,'2023/12/01','True'),
(833,14,'2023/12/01','True'),
(834,14,'2023/12/01','True'),
(835,14,'2023/12/01','False'),
(836,14,'2023/12/01','True'),
(837,14,'2023/12/01','True'),
(838,14,'2023/12/01','True'),
(839,14,'2023/12/01','False'),
(840,14,'2023/12/01','False'),
(841,14,'2023/12/01','True'),
(842,14,'2023/12/01','False'),
(843,14,'2023/12/01','False'),
(844,14,'2023/12/01','False'),
(845,14,'2023/12/01','True'),
(846,14,'2023/12/01','False'),
(847,14,'2023/12/01','True'),
(848,14,'2023/12/01','True'),
(849,14,'2023/12/01','True'),
(850,14,'2023/12/01','True'),
(851,14,'2023/12/01','False'),
(852,14,'2023/12/01','True'),
(853,14,'2023/12/01','True'),
(854,14,'2023/12/01','False'),
(855,14,'2023/12/01','True'),
(856,14,'2023/12/01','True'),
(857,14,'2023/12/01','True'),
(858,14,'2023/12/01','False'),
(859,14,'2023/12/01','False'),
(860,14,'2023/12/01','True'),
(861,14,'2023/12/01','False'),
(862,14,'2023/12/01','False'),
(863,14,'2023/12/01','False'),
(864,14,'2023/12/01','False'),
(865,14,'2023/12/01','False'),
(866,14,'2023/12/01','False'),
(867,14,'2023/12/01','False'),
(868,14,'2023/12/01','False'),
(869,15,'2023/12/01','False'),
(870,15,'2023/12/01','True'),
(871,15,'2023/12/01','True'),
(872,15,'2023/12/01','True'),
(873,15,'2023/12/01','False'),
(874,15,'2023/12/01','False'),
(875,15,'2023/12/01','False'),
(876,15,'2023/12/01','True'),
(877,15,'2023/12/01','True'),
(878,15,'2023/12/01','True'),
(879,15,'2023/12/01','False'),
(880,15,'2023/12/01','True'),
(881,15,'2023/12/01','True'),
(882,15,'2023/12/01','False'),
(883,15,'2023/12/01','True'),
(884,15,'2023/12/01','False'),
(885,15,'2023/12/01','False'),
(886,15,'2023/12/01','False'),
(887,15,'2023/12/01','False'),
(888,15,'2023/12/01','False'),
(889,15,'2023/12/01','False'),
(890,15,'2023/12/01','False'),
(891,15,'2023/12/01','False'),
(892,15,'2023/12/01','False'),
(893,15,'2023/12/01','False'),
(894,15,'2023/12/01','True'),
(895,15,'2023/12/01','True'),
(896,15,'2023/12/01','False'),
(897,15,'2023/12/01','False'),
(898,15,'2023/12/01','False'),
(899,15,'2023/12/01','True'),
(900,15,'2023/12/01','True'),
(901,15,'2023/12/01','True'),
(902,15,'2023/12/01','True'),
(903,15,'2023/12/01','False'),
(904,15,'2023/12/01','True'),
(905,15,'2023/12/01','True'),
(906,15,'2023/12/01','False'),
(907,15,'2023/12/01','False'),
(908,15,'2023/12/01','False'),
(909,15,'2023/12/01','False'),
(910,15,'2023/12/01','False'),
(911,15,'2023/12/01','False'),
(912,15,'2023/12/01','False'),
(913,15,'2023/12/01','True'),
(914,15,'2023/12/01','False'),
(915,15,'2023/12/01','False'),
(916,15,'2023/12/01','False'),
(917,15,'2023/12/01','True'),
(918,15,'2023/12/01','False'),
(919,15,'2023/12/01','True'),
(920,15,'2023/12/01','True'),
(921,15,'2023/12/01','True'),
(922,15,'2023/12/01','False'),
(923,15,'2023/12/01','True'),
(924,15,'2023/12/01','True'),
(925,15,'2023/12/01','True'),
(926,15,'2023/12/01','False'),
(927,15,'2023/12/01','False'),
(928,15,'2023/12/01','False'),
(929,15,'2023/12/01','False'),
(930,15,'2023/12/01','True'),
(931,16,'2023/12/01','True'),
(932,16,'2023/12/01','True'),
(933,16,'2023/12/01','False'),
(934,16,'2023/12/01','True'),
(935,16,'2023/12/01','False'),
(936,16,'2023/12/01','True'),
(937,16,'2023/12/01','False'),
(938,16,'2023/12/01','False'),
(939,16,'2023/12/01','True'),
(940,16,'2023/12/01','False'),
(941,16,'2023/12/01','False'),
(942,16,'2023/12/01','True'),
(943,16,'2023/12/01','True'),
(944,16,'2023/12/01','False'),
(945,16,'2023/12/01','False'),
(946,16,'2023/12/01','True'),
(947,16,'2023/12/01','False'),
(948,16,'2023/12/01','False'),
(949,16,'2023/12/01','False'),
(950,16,'2023/12/01','True'),
(951,16,'2023/12/01','False'),
(952,16,'2023/12/01','True'),
(953,16,'2023/12/01','True'),
(954,16,'2023/12/01','False'),
(955,16,'2023/12/01','False'),
(956,16,'2023/12/01','False'),
(957,16,'2023/12/01','False'),
(958,16,'2023/12/01','False'),
(959,16,'2023/12/01','False'),
(960,16,'2023/12/01','False'),
(961,16,'2023/12/01','True'),
(962,16,'2023/12/01','True'),
(963,16,'2023/12/01','False'),
(964,16,'2023/12/01','False'),
(965,16,'2023/12/01','False'),
(966,16,'2023/12/01','False'),
(967,16,'2023/12/01','True'),
(968,16,'2023/12/01','True'),
(969,16,'2023/12/01','True'),
(970,16,'2023/12/01','False'),
(971,16,'2023/12/01','False'),
(972,16,'2023/12/01','True'),
(973,16,'2023/12/01','True'),
(974,16,'2023/12/01','False'),
(975,16,'2023/12/01','True'),
(976,16,'2023/12/01','True'),
(977,16,'2023/12/01','True'),
(978,16,'2023/12/01','False'),
(979,16,'2023/12/01','False'),
(980,16,'2023/12/01','True'),
(981,16,'2023/12/01','False'),
(982,16,'2023/12/01','False'),
(983,16,'2023/12/01','False'),
(984,16,'2023/12/01','True'),
(985,16,'2023/12/01','True'),
(986,16,'2023/12/01','False'),
(987,16,'2023/12/01','False'),
(988,16,'2023/12/01','True'),
(989,16,'2023/12/01','True'),
(990,16,'2023/12/01','True'),
(991,16,'2023/12/01','False'),
(992,16,'2023/12/01','False'),
(993,16,'2023/12/01','False'),
(994,16,'2023/12/01','False'),
(995,16,'2023/12/01','True'),
(996,16,'2023/12/01','False'),
(997,16,'2023/12/01','True'),
(998,16,'2023/12/01','False'),
(999,16,'2023/12/01','True'),
(1000,16,'2023/12/01','True')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `posts` (
  `id` int(5) NOT NULL,
  `author` varchar(10) NOT NULL,
  `text` varchar(200) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `posts` (`id`, `author`, `text`, `time`) VALUES
(1, 'kalle', 'hello', '2025-11-05 10:33:02'),
(2, 'kalle', 'Blablablabla', '2025-11-05 10:34:35'),
(3, 'alexander', 'Do you feel lucky?', '2025-11-05 10:46:55');

ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `posts`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

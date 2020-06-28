USE [python_db]
GO

/****** Object:  Table [dbo].[courses1]    Script Date: 6/28/2020 9:21:43 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[courses1](
	[course_id] [int] NULL,
	[course_name] [varchar](30) NULL,
	[course_fees] [int] NULL,
	[course_duration_month] [int] NULL,
	[std_id] [int] NULL,
	[fees_paid_by_student] [int] NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[courses1]  WITH CHECK ADD FOREIGN KEY([std_id])
REFERENCES [dbo].[student1] ([std_id])
GO

ALTER TABLE [dbo].[courses1]  WITH CHECK ADD  CONSTRAINT [fk_name] FOREIGN KEY([std_id])
REFERENCES [dbo].[student1] ([std_id])
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[courses1] CHECK CONSTRAINT [fk_name]
GO



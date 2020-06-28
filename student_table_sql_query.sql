USE [python_db]
GO

/****** Object:  Table [dbo].[student1]    Script Date: 6/28/2020 9:34:54 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[student1](
	[name] [varchar](40) NULL,
	[age] [int] NULL,
	[std_id] [int] NOT NULL,
	[father_name] [varchar](30) NULL,
	[date_of_addmssion] [date] NULL DEFAULT (getdate()),
	[std_address] [varchar](50) NULL,
	[personal_phone_no] [varchar](20) NULL,
	[father_phone_no] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[std_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO



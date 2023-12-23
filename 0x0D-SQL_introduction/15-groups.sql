-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
 select score, count(score) as number from second_table group by score order by (score) desc;


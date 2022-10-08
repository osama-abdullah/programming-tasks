from jira import JIRA # pip install jira
import pandas as pd # pip install pandas

def crawlIssueData(server_link,issues):
    jira = JIRA(server_link) 

    issues_df=pd.DataFrame()
    comments_df=pd.DataFrame()

    for issue in issues: # read all issues and collect thier data

        issue = jira.issue(issue) 

        assignee=issue.fields.assignee
        #attachment=issue.fields.attachment
        comments=issue.fields.comment.comments
        created=issue.fields.created
        description=issue.fields.description
        duedate=issue.fields.duedate
        issuetype=issue.fields.issuetype
        #labels=issue.fields.labels
        priority=issue.fields.priority
        project=issue.fields.project
        reporter=issue.fields.reporter
        resolution=issue.fields.resolution
        summary=issue.fields.summary
        #versions=issue.fields.versions
        status=issue.fields.status
        votes=issue.fields.votes

        # save current issue data into temporary data frame 

        temp_df=pd.DataFrame([{'assignee':assignee, 'created':created, 'description':description,
        'duedate':duedate,'issuetype':issuetype,'priority':priority,'project':project,'reporter':reporter,
        'resolution':resolution,'summary':summary,'status':status,'votes':votes
        }])
        
        issues_df=pd.concat([issues_df,temp_df]) # append current issue to the entire issues data

        # iterate into all comments of the issue and collect their data
        for comment in comments:
            t_df=pd.DataFrame([{'issue_id':issue,'auther':comment.author.displayName,'comment_date':comment.created,'body':comment.body}])
            comments_df=pd.concat([comments_df,t_df])
            
    return issues_df,comments_df

issueData,commentsData = crawlIssueData('https://issues.apache.org/jira/',['CAMEL-10597'])

# save issues data and comments data separtely because the relationship between them is one to many
issueData.to_csv('issues-report.csv')

commentsData.to_csv('issues-comments.csv')

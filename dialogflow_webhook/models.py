from django.db import models

class SubscriptionTemp(models.Model):
    payment_payload = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_temp'


class TblAdmin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_email = models.CharField(max_length=255, blank=True, null=True)
    admin_password = models.CharField(max_length=255, blank=True, null=True)
    admin_mobile = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_admin'


class TblClientComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    portfolio_id = models.IntegerField()
    comment_text = models.CharField(max_length=1000)
    comment_rating = models.IntegerField()
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_client_comments'


class TblCompletedHistory(models.Model):
    completed_history_id = models.AutoField(primary_key=True)
    emp_issue_id = models.IntegerField()
    changed_by = models.IntegerField()
    completed_date = models.DateTimeField()
    change_reason = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_completed_history'


class TblEmployeeIssue(models.Model):
    employee_issue_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    add_issue_type = models.CharField(max_length=8)
    is_emp = models.IntegerField()
    is_manager = models.IntegerField()
    issue_title = models.TextField(blank=True, null=True)
    issue_description = models.TextField(blank=True, null=True)
    issue_note = models.TextField(blank=True, null=True)
    issue_priority = models.CharField(max_length=9)
    issue_status = models.CharField(max_length=12)
    performance_percentage = models.IntegerField(blank=True, null=True)
    expected_completion_date = models.DateTimeField(blank=True, null=True)
    solved_issue_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_issue'


class TblExpectedCompletionHistory(models.Model):
    expected_completion_history_id = models.AutoField(primary_key=True)
    emp_issue_id = models.IntegerField()
    changed_by = models.IntegerField()
    expected_completion_date = models.DateTimeField()
    change_reason = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_expected_completion_history'


class TblIssuePriorityHistory(models.Model):
    issue_priority_history_id = models.AutoField(primary_key=True)
    emp_issue_id = models.IntegerField()
    issue_priority = models.CharField(max_length=9)
    change_by = models.IntegerField()
    change_reason = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_issue_priority_history'


class TblIssueStatusHistory(models.Model):
    issue_status_history_id = models.AutoField(primary_key=True)
    emp_issue_id = models.IntegerField()
    change_by = models.IntegerField()
    issue_status = models.CharField(max_length=12)
    change_reason = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_issue_status_history'


class TblJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_vacancy = models.IntegerField()
    job_title = models.CharField(max_length=100, blank=True, null=True)
    job_sub_title = models.CharField(max_length=255, blank=True, null=True)
    job_tech_iocn = models.TextField(blank=True, null=True)
    job_position = models.CharField(max_length=255, blank=True, null=True)
    job_experience = models.TextField(blank=True, null=True)
    job_salary = models.CharField(max_length=255, blank=True, null=True)
    job_call = models.CharField(max_length=100, blank=True, null=True)
    job_email = models.CharField(max_length=100, blank=True, null=True)
    job_location = models.TextField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_reponsiblites = models.TextField(blank=True, null=True)
    job_requirements = models.TextField(blank=True, null=True)
    job_requirement_status = models.CharField(max_length=11)
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_job'


class TblJobVacancy(models.Model):
    job_vacancy_id = models.AutoField(primary_key=True)
    job_vacancy = models.TextField(blank=True, null=True)
    vacancy_icon = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_job_vacancy'


class TblLifeAtWeapp(models.Model):
    life_at_weapp_id = models.AutoField(primary_key=True)
    image_title = models.TextField(blank=True, null=True)
    image_content_type = models.CharField(max_length=8)
    image_content = models.TextField()
    image_thumb = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_life_at_weapp'


class TblPortfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    project_name = models.TextField(blank=True, null=True)
    project_main_image = models.TextField(blank=True, null=True)
    project_icon = models.TextField(blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    technology_id = models.CharField(max_length=255, blank=True, null=True)
    sub_technology_id = models.CharField(max_length=255)
    project_description = models.TextField(blank=True, null=True)
    project_overview = models.TextField(blank=True, null=True)
    play_store_url = models.TextField(blank=True, null=True)
    app_store_url = models.TextField(blank=True, null=True)
    web_site_url = models.TextField(blank=True, null=True)
    project_location = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_portfolio'


class TblPortfolioImage(models.Model):
    port_image_id = models.AutoField(primary_key=True)
    portfolio_id = models.IntegerField()
    portfolio_image = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_portfolio_image'


class TblSubTechnology(models.Model):
    sub_technology_id = models.AutoField(primary_key=True)
    sub_technology_name = models.CharField(max_length=255, blank=True, null=True)
    sub_tech_short_name = models.CharField(max_length=25, blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sub_technology'


class TblTechnology(models.Model):
    technology_id = models.AutoField(primary_key=True)
    technology_name = models.CharField(max_length=255, blank=True, null=True)
    tech_short_name = models.CharField(max_length=25, blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_technology'


class TblUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.CharField(max_length=10)
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_user'

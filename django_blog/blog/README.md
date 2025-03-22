This Django blog project implements a comprehensive blog post management system with full CRUD (Create, Read, Update, Delete) functionalities. It allows authenticated users to create, edit, and delete their posts while ensuring proper permissions and security measures.

List all blog posts (accessible to all users)

View individual blog posts

Create new blog posts (only for authenticated users)

Edit own posts (only the author can edit)

Delete own posts (only the author can delete)

Secure access control with Django authentication system


Permissions & Security

Only authenticated users can create posts.

Users can edit and delete only their own posts.

Uses Django's LoginRequiredMixin and UserPassesTestMixin for access control.

CSRF protection is enabled on all forms

Usage

1. Viewing Posts

Navigate to the homepage (/) to see a list of all blog posts.

Click on a post title to view its full content.

2. Creating a Post

Login (/login/) or register (/register/) if not already logged in.

Click on "New Post" (/posts/new/) and fill in the form.

Submit the form to create a new blog post.

3. Editing a Post

Click "Edit" on a post (only visible if you are the author).

Modify the content and submit to save changes.

4. Deleting a Post

Click "Delete" on your post.

Confirm deletion on the next page.

Setup
Clone repository:
git clone https://github.com/yourusername/django-blog.git
cd django-blog
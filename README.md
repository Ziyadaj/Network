# Social Network

This is a social network application that allows users to make posts, follow other users, and "like" posts.

## Features

New Post: Users who are signed in can write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
All Posts: The "All Posts" link in the navigation bar takes the user to a page where they can see all posts from all users, with the most recent posts first. Each post includes the username of the poster, the post content itself, the date and time at which the post was made, and the number of "likes" the post has.

Profile Page: Clicking on a username loads that user's profile page. This page displays the number of followers the user has, as well as the number of people that the user follows. It also displays all of the posts for that user, in reverse chronological order. For any other user who is signed in, this page also displays a "Follow" or "Unfollow" button that lets the current user toggle whether or not they are following this user's posts. Note that this only applies to any "other" user: a user should not be able to follow themselves.

Following: The "Following" link in the navigation bar takes the user to a page where they see all posts made by users that the current user follows. This page behaves just as the "All Posts" page does, just with a more limited set of posts. This page is only available to users who are signed in.

Pagination: On any page that displays posts, posts are displayed 10 on a page. If there are more than ten posts, a "Next" button appears to take the user to the next page of posts (which is older than the current page of posts). If not on the first page, a "Previous" button appears to take the user to the previous page of posts as well.

Edit Post: Users can click an "Edit" button or link on any of their own posts to edit that post. When a user clicks "Edit" for one of their own posts, the content of their post is replaced with a textarea where the user can edit the content of their post. The user can then "Save" the edited post. Using JavaScript, this can be achieved without requiring a reload of the entire page. For security, the application is designed such that it is not possible for a user, via any route, to edit another user's posts.

"Like" and "Unlike": Users can click a button or link on any post to toggle whether or not they "like" that post. Using JavaScript, the application asynchronously lets the server know to update the like count (as via a call to fetch) and then updates the post's like count displayed on the page, without requiring a reload of the entire page.

## Technologies Used

This social network application is built using the following technologies:

Python
JavaScript
HTML
CSS


## Credits

This project was created as part of the requirements for the CS50W course offered by Harvard University.

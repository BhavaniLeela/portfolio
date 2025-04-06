document.addEventListener('DOMContentLoaded', async () => {
  const response = await fetch('http://localhost:8000/api/blogs/');
  const blogs = await response.json();
  const list = document.getElementById('blog-list');
  blogs.forEach(blog => {
    const div = document.createElement('div');
    div.innerHTML = `<h3>${blog.title}</h3><p>${blog.content.substring(0, 100)}...</p><a href="detail.html?id=${blog.id}">Read More</a>`;
    list.appendChild(div);
  });
});
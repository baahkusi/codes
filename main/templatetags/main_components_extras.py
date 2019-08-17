from django import template

register = template.Library()


"""
HTML Components
"""
@register.inclusion_tag('main/components/plus.html')
def plus():
    pass


@register.inclusion_tag('main/components/sign_in.html')
def sign_in():
    pass


@register.inclusion_tag('main/components/sign_up.html')
def sign_up():
    pass


@register.inclusion_tag('main/components/reset.html')
def reset():
    pass


@register.inclusion_tag('main/components/navbar.html')
def navbar():
    pass


@register.inclusion_tag('main/components/header.html')
def header():
    pass


@register.inclusion_tag('main/components/slider.html')
def slider():
    pass


@register.inclusion_tag('main/components/divider.html')
def divider():
    pass


@register.inclusion_tag('main/components/carousel.html')
def carousel():
    pass


@register.inclusion_tag('main/components/portfolio.html')
def portfolio():
    pass


@register.inclusion_tag('main/components/grid_text.html')
def grid_text():
    pass


@register.inclusion_tag('main/components/footer.html')
def footer():
    pass


@register.inclusion_tag('main/components/about.html')
def about():
    pass


@register.inclusion_tag('main/components/call.html')
def call_action():
    pass

@register.inclusion_tag('main/components/banner.html')
def banner(title, link):
    return {"title":title,'link':link}

@register.inclusion_tag('main/components/image-grid.html')
def image_grid(title):
    return {"title":title}


@register.inclusion_tag('main/components/image-slider.html')
def image_slider():
    pass


@register.inclusion_tag('main/components/accordion.html')
def accordion():
    pass


@register.inclusion_tag('main/components/blog_list.html')
def blog_list():
    pass


@register.inclusion_tag('main/components/article.html')
def article(title):
    return {"title":title}

@register.inclusion_tag('main/components/sidebar.html')
def sidebar():
    pass


@register.inclusion_tag('main/components/pager.html')
def pager():
    pass


@register.inclusion_tag('main/components/tags_list.html')
def tags_list():
    pass


@register.inclusion_tag('main/components/image_list.html')
def image_list():
    pass


@register.inclusion_tag('main/components/category_list.html')
def category_list():
    pass


@register.inclusion_tag('main/components/blog_post.html')
def blog_post():
    pass


@register.inclusion_tag('main/components/post_article.html')
def post_article():
    pass


@register.inclusion_tag('main/components/testimonials.html')
def testimonials():
    pass


@register.inclusion_tag('main/components/tabs-top.html')
def tabs_top():
    pass


@register.inclusion_tag('main/components/tabs-left.html')
def tabs_left():
    pass


@register.inclusion_tag('main/components/tabs-right.html')
def tabs_right():
    pass


@register.inclusion_tag('main/components/alert.html')
def alert():
    pass


@register.inclusion_tag('main/components/portfolio-detail.html')
def portfolio_detail():
    pass


@register.inclusion_tag('main/components/404.html')
def fourOfour():
    pass


@register.inclusion_tag('main/components/table.html')
def table():
    pass


@register.inclusion_tag('main/components/pricingbox.html')
def pricingbox():
    pass
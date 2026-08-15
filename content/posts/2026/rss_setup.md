# Setting Up RSS Feeds With Newsboat

I found out about RSS feeds from boot.dev; their guided project on building an RSS Feed Aggregator. I'd seen them around from the icon on lots of websites, and heard something about podcasts running on them years ago, but the project on boot.dev was the thing that made me give them a go. Hopefully I'll find it a good alternative to algorithmically controlled content. I've been reading email newsletters for a while now after deleting social media apps from my phone, and I hope this will be in a similar vein to that.

I'm trying out [newsboat](https://newsboat.org/), which I installed on macOS using ```brew install newsboat```. Their [docs](https://newsboat.org/releases/2.43/docs/newsboat.html) are good. It has a better UI than my guided project, and it's nice not being responsible for maintaining it.

## Setup

### Following Feeds

To follow feeds, you first need to create a file to store their urls at location ```~/.newsboat/urls```

NB: ```urls``` is the filename, it has no file extension

It will look something like this:

```
www.abc.com/rss
www.xyz.com/feed.xml
```

Literally just a list of feed URLs that you want to follow. Make sure to get the RSS feed link on a blog, and not the link to the blog itself. They are different things. RSS feed links tend to end in either ```.xml``` or ```.rss```, or they can have no extension and just be called something like ```rss``` or ```feed```. There is often an icon in the url address bar or somewhere on the website that will take you to the right address.

### Configuration

If you want to do any configuration then you'll need a config file at location ```~/.newsboat/config```

NB: ```config``` is the filename, it has no file extension

You will need to set a browser in the configuration if you use a browser other than lynx. [Here](https://newsboat.org/releases/2.43/docs/newsboat.html#_newsboat_configuration_commands) are the configuration commands, and [here](https://newsboat.org/releases/2.43/docs/newsboat.html#_using_browser) is the section in the docs on using a browser.

My configuration file just contains ```browser "open -a Firefox %u"``` currently.

## Usage

Type ```newsboat``` into the terminal to open newsboat. Keyboard commands are at the bottom of the screen. You'll need to do ```Shift``` + ```r``` initially to load in some articles, and again whenever you'd like to refresh the list of articles. It should show you a list of the feeds you have added to your ```urls``` file. When you select one, it takes you to a list of articles from that feed. When you select an article it opens a preview, and you press ```o``` to open it in your browser. ```q``` to quit.

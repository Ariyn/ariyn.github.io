module SiteHelpers
  def self.tag_slug(value)
    value.to_s.strip.downcase.gsub(/\s+/, "-")
  end
end

module SiteFilters
  def site_tag_slug(value)
    SiteHelpers.tag_slug(value)
  end
end

Liquid::Template.register_filter(SiteFilters)

class TagPageGenerator < Jekyll::Generator
  safe true
  priority :low

  def generate(site)
    site.tags.each_key do |tag|
      site.pages << TagPage.new(site, site.source, tag)
    end
  end
end

class TagPage < Jekyll::Page
  def initialize(site, base, tag)
    @site = site
    @base = base
    @dir = File.join("tags", SiteHelpers.tag_slug(tag))
    @name = "index.html"

    process(@name)
    read_yaml(File.join(base, "_layouts"), "tag.html")
    data["tag"] = tag
    data["title"] = tag
  end
end

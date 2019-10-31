require 'selenium-webdriver'
require 'time'

class NetworkMedia

  def initialize(browser)
    @browser = browser
    @waiter = Selenium::WebDriver::Wait.new(:timeout => 15)
    @reports= {}
  end

  def execute(order)
    # 0 Laver de potentiels previous execute:
    @reports = {}

    # 1 Se connecter au site:
    if connexion(order)

    # 2 Executer l'ordre :
      public_send(order.order_tag.downcase, order.order_args)
    else
      @reports[:ERROR]= "Failed to connect with these #{order.network.network_name}'s logs."
    end

    # 3 Envoie le reporting de cette execution
    return @reports
  end

  def connexion(order)
    network_name = order.network.network_name.downcase
    nwk_id = order.network.id
    account = order.user.accounts.where(network_id: nwk_id).first
    user = account.network_login
    password = account.network_password
    return self.public_send("connect_#{network_name}", user, password)
  end

  # A RENDRE PLUS GENERIQUE
  def connect_site
    lets_try =1 #On considère que si ca fail une fois, ca fail toujours
    we_tryied = 0
    while lets_try>we_tryied
      begin
        yield
        return true
      rescue
        puts "fail in login"
        access_url("https://www.google.fr")
        sleep(1)
        we_tryied+=1
      end
    end
    return false

  end


  private

  def fill_text_box(html_method,id_string, fill_text, waiter = @waiter)
    input = waiter.until {
        element = @browser.find_element(html_method, id_string)
        element if element.displayed?
    }
    input.send_keys(fill_text)

  end

  def click_element(html_method,id_string)
    begin
      elt = @browser.find_element(html_method, id_string)
    rescue
      return false
    else
      elt.click
    end
  end

  def access_url(url)
    @browser.get url
  end

  def scroll_down(wait_seconds=2)
    @browser.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
    @browser.execute_script("window.scrollBy(0,100)")
    sleep(wait_seconds)
  end

  def scroll_by(nb, wait_seconds = 1)
    @browser.execute_script("window.scrollBy(0,#{nb})")
    sleep(wait_seconds)
  end

  def scroll_up(wait_seconds=2)
    @browser.execute_script("window.scrollTo(document.body.scrollHeight , 0)")
    sleep(wait_seconds)
  end


end

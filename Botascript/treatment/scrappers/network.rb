require 'selenium-webdriver'

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
      @reports["BUG::"]= "Failed to connect with these #{order.network.network_name}'s logs."
    end

    # 3 Envoie le reporting de cette execution
    return @reports
  end

  def connexion(order)

    network_name = order.network.network_name.downcase
    nwk_id = Network.find_by_network_name(network_name.capitalize).id

    account = Order.first.user.accounts.where(network_id: nwk_id).first
    user = account.network_login
    password = account.network_password

    return self.public_send("connect_#{network_name}", user, password)
  end

  def fill_text_box(html_method,id_string, fill_text, waiter = @waiter)
    input = waiter.until {
        element = @browser.find_element(html_method, id_string)
        element if element.displayed?
    }
    input.send_keys(fill_text)

  end

  def click_element(html_method,id_string)
    @browser.find_element(html_method, id_string).click
  end

  def access_url(url)
    @browser.get url
  end

  def waiter_complete_load(nb)
    threshold = nb+15
    i=0
    condition = true
    returned_list = []
    while(condition)
      returned_list = yield
      condition= returned_list.size < nb
      i+=1
      if i>=threshold
        @reports["BUG:::Waiter"] = "Not enough card loaded"
        return false
      end
      sleep(0.3)
    end
    return returned_list
  end

  def looking_for_list_of_items(options = {"nb": 1,"content":/[a-zA-Z0-9]*/})
    list_items = waiter_complete_load(options[:nb]){
      @browser.find_elements(options[:html_method],options[:id_string]).select{ |elt|
        if options[:content].class == String
          elt.text.downcase == options[:content]
        else
          elt.text.downcase =~ options[:content]
        end
      }
    }
    return list_items
  end


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

end

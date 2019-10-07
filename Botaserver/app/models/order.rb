include ::TimeConcern
class Order < ApplicationRecord
  belongs_to :user
  belongs_to :network
  has_many :logs,  dependent: :delete_all

  def self.convertTime(arg)
  	return Time::secondConverter(arg)
  end

  def self.convertSeconds(arg)
  	return Time::integerConverter(arg)
  end

  def self.exec_scope
    return where("alive = ?", 1).where("exectime <= ?", Time.now() ).select{|order| not order.processing}
    # Should return an ActiveRecord::Relation.
  end
end
